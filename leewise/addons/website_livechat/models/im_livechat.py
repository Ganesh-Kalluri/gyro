# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, models, fields
from leewise.addons.http_routing.models.ir_http import slug
from leewise.tools.translate import html_translate


class ImLivechatChannel(models.Model):

    _name = 'im_livechat.channel'
    _inherit = ['im_livechat.channel', 'website.published.mixin']

    def _compute_website_url(self):
        super(ImLivechatChannel, self)._compute_website_url()
        for channel in self:
            channel.website_url = "/livechat/channel/%s" % (slug(channel),)

    website_description = fields.Html(
        "Website description", default=False, translate=html_translate,
        sanitize_overridable=True,
        sanitize_attributes=False, sanitize_form=False,
        help="Description of the channel displayed on the website page")
