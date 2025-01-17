# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

import requests
from datetime import datetime
from urllib.parse import quote
from werkzeug.urls import url_join
from urllib.parse import urlparse
import re

from leewise import models, _
from leewise.exceptions import UserError


class SocialStreamLinkedIn(models.Model):
    _inherit = 'social.stream'

    def _apply_default_name(self):
        linkedin_streams = self.filtered(lambda s: s.media_id.media_type == 'linkedin')
        super(SocialStreamLinkedIn, (self - linkedin_streams))._apply_default_name()

        for stream in linkedin_streams:
            stream.write({'name': '%s: %s' % (stream.stream_type_id.name, stream.account_id.name)})

    def _fetch_stream_data(self):
        """Fetch stream data, return True if new data.

        We need to perform 2 HTTP requests. One to retrieve all the posts of
        the organization page and the other, in batch, to retrieve the
        statistics of all posts (there are 2 different endpoints)."""
        self.ensure_one()
        if self.media_id.media_type != 'linkedin':
            return super(SocialStreamLinkedIn, self)._fetch_stream_data()

        # retrieve post information
        if self.stream_type_id.stream_type != 'linkedin_company_post':
            raise UserError(_('Wrong stream type for "%s"', self.name))

        posts_response = self.account_id._linkedin_request(
            "posts",
            params={
                'q': 'author',
                'count': 100,
                'author': self.account_id.linkedin_account_urn,
            },
            fields=('id', 'createdAt', 'author', 'content', 'commentary')
        )
        if posts_response.status_code != 200 or 'elements' not in posts_response.json():
            self.sudo().account_id._action_disconnect_accounts(posts_response.json())
            return False

        stream_post_data = posts_response.json()['elements']

        self._prepare_linkedin_stream_post_images(stream_post_data)

        linkedin_post_data = {
            stream_post_data.get('id'): self._prepare_linkedin_stream_post_values(stream_post_data)
            for stream_post_data in stream_post_data
        }

        # retrieve post statistics
        stats_endpoint = url_join(
            self.env['social.media']._LINKEDIN_ENDPOINT,
            'socialActions?ids=List(%s)' % ','.join([quote(urn) for urn in linkedin_post_data]))
        stats_response = requests.get(stats_endpoint, params={'count': 100}, headers=self.account_id._linkedin_bearer_headers(), timeout=5).json()

        if 'results' in stats_response:
            for post_urn, post_data in stats_response['results'].items():
                linkedin_post_data[post_urn].update({
                    'linkedin_comments_count': post_data.get('commentsSummary', {}).get('totalFirstLevelComments', 0),
                    'linkedin_likes_count': post_data.get('likesSummary', {}).get('totalLikes', 0),
                })

        # create/update post values
        existing_post_urns = {
            stream_post.linkedin_post_urn: stream_post
            for stream_post in self.env['social.stream.post'].search([
                ('stream_id', '=', self.id),
                ('linkedin_post_urn', 'in', list(linkedin_post_data.keys()))])
        }

        post_to_create = []
        for post_urn in linkedin_post_data:
            if post_urn in existing_post_urns:
                existing_post_urns[post_urn].sudo().write(linkedin_post_data[post_urn])
            else:
                post_to_create.append(linkedin_post_data[post_urn])

        if post_to_create:
            self.env['social.stream.post'].sudo().create(post_to_create)

        return bool(post_to_create)

    def _format_linkedin_name(self, json_data):
        user_name = '%s %s' % (json_data.get('localizedLastName', ''), json_data.get('localizedFirstName', ''))
        return json_data.get('localizedName', user_name)

    def _prepare_linkedin_stream_post_images(self, posts_data):
        """Fetch the images URLs and insert their URL in posts_data."""
        all_image_urns = set()
        for post in posts_data:
            # multi-images post
            images = post.get('content', {}).get('multiImage', {}).get('images', [])
            all_image_urns |= {quote(image['id']) for image in images}
            # single image post
            if image_urn := post.get('content', {}).get('media', {}).get('id'):
                all_image_urns.add(quote(image_urn))
            # article thumbnail
            if thumbnail_urn := post.get('content', {}).get('article', {}).get('thumbnail'):
                all_image_urns.add(quote(thumbnail_urn))

        if not all_image_urns:
            return

        images_endpoint = url_join(
            self.env['social.media']._LINKEDIN_ENDPOINT,
            'images?ids=List(%s)' % ",".join(all_image_urns))
        response = requests.get(
            images_endpoint,
            params={},
            headers=self.account_id._linkedin_bearer_headers(),
            timeout=10,
        )

        if not response.ok:
            return

        url_by_urn = {
            image: image_values["downloadUrl"]
            for image, image_values in response.json()["results"].items()
            if image_values.get("downloadUrl")
        }

        # Insert image in the result like the LinkedIn projection should do...
        for post in posts_data:
            # multi-images post
            images = post.get('content', {}).get('multiImage', {}).get('images', [])
            for image in images:
                image["downloadUrl"] = url_by_urn.get(image.get("id"))

            # single image post
            if image_urn := post.get("content", {}).get("media", {}).get("id"):
                post["content"]["media"]["downloadUrl"] = url_by_urn.get(image_urn)

            # article thumbnail
            if thumbnail_urn := post.get("content", {}).get("article", {}).get("thumbnail"):
                post["content"]["article"]["~thumbnail"] = {"downloadUrl": url_by_urn.get(thumbnail_urn)}

    def _prepare_linkedin_stream_post_values(self, post_data):
        article = post_data.get('content', {}).get('article', {})
        author_image = f"/web/image?model=social.account&id={self.account_id.id}&field=image"
        return {
            'stream_id': self.id,
            'author_name': self.account_id.name,
            'published_date': datetime.fromtimestamp(post_data.get('createdAt', 0) / 1000),
            'linkedin_post_urn': post_data.get('id'),
            'linkedin_author_urn': post_data.get('author'),
            'linkedin_author_image_url': author_image,
            'message': self._format_from_linkedin_little_text(post_data.get('commentary', '')),
            'stream_post_image_ids': [(5, 0)] + [(0, 0, image_value) for image_value in self._extract_linkedin_image(post_data)],
            **self._extract_linkedin_article(article),
        }

    def _extract_linkedin_image(self, post_data):
        # single image post
        single_image = post_data.get('content', {}).get('media', {}).get('downloadUrl')
        if single_image:
            return [{'image_url': self._enforce_url_scheme(single_image)}]

        # multi-images post
        if images := post_data.get('content', {}).get('multiImage', {}).get('images', []):
            return [
                {'image_url': self._enforce_url_scheme(image.get('downloadUrl'))}
                for image in images if image.get('downloadUrl')
            ]

        # article with thumbnail
        if thumbnail_url := post_data.get('content', {}).get('article', {}).get('~thumbnail', {}).get('downloadUrl'):
            return [{'image_url': self._enforce_url_scheme(thumbnail_url)}]

        return []

    def _extract_linkedin_article(self, article):
        if not article:
            return {}

        return {
            'link_title': article.get('title', '') or article.get('source', ''),
            'link_description': article.get('description', ''),
            'link_url': self._enforce_url_scheme(article.get('source'))
        }

    def _enforce_url_scheme(self, url):
        """Some URLs doesn't starts by "https://". But if we use those bad URLs
        in a HTML link, it will redirect the user the actual website.
        That's why we need to fix those URLs.
        e.g.:
            <a href="www.bad_url.com"/>
        """
        if not url or urlparse(url).scheme:
            return url

        return 'https://%s' % url

    def _format_from_linkedin_little_text(self, input_string):
        """
        Replaces escaped versions of the characters `(){}<>[]_` with their original characters,
        """
        pattern = "\\\\([\\(\\)\\<\\>\\{\\}\\[\\]\\_\\|\\*\\~\\#\\@])"
        output_string = re.sub(pattern, lambda match: match.group(1), input_string)
        return output_string
