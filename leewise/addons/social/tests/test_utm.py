# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.addons.social.tests.common import SocialCase
from leewise.addons.social.tests.tools import mock_void_external_calls
from leewise.addons.utm.tests.common import TestUTMCommon
from leewise.exceptions import UserError
from leewise.tests.common import tagged, users


@tagged('post_install', '-at_install', 'utm_consistency')
class TestUTMConsistencySocial(TestUTMCommon, SocialCase):

    @classmethod
    def setUpClass(cls):
        super(TestUTMConsistencySocial, cls).setUpClass()

        cls.user_social_manager = cls.env['res.users'].create({
            'name': 'Social Manager',
            'login': 'user_social_manager',
            'email': 'user_social_manager@test.com',
            'groups_id': [(6, 0, [cls.env.ref('social.group_social_manager').id])],
        })

    @users('user_social_manager')
    @mock_void_external_calls()
    def test_utm_consistency_mass_mailing_user(self):
        # social manager user should be able to unlink all UTM models
        self.utm_campaign.unlink()
        self.utm_medium.unlink()
        self.utm_source.unlink()

    @users('__system__')
    @mock_void_external_calls()
    def test_utm_consistency_social_account(self):
        # the medium is automatically created when creating a social account
        utm_medium = self.social_account.utm_medium_id

        with self.assertRaises(UserError):
            # can't unlink the medium as it's used by a social.post as it's medium
            # unlinking the medium would break sent link trackers
            utm_medium.unlink()

    @users('__system__')
    @mock_void_external_calls()
    def test_utm_consistency_social_post(self):
        social_post = self.env['social.post'].create({
            'account_ids': [(4, self.social_account.id)],
            'message': 'Message 1',
        })
        # the source is automatically created when creating a post
        utm_source = social_post.source_id

        with self.assertRaises(UserError):
            # can't unlink the source as it's used by a social.post as its source
            # unlinking the source would break sent link trackers
            utm_source.unlink()

    @classmethod
    def _get_social_media(cls):
        return cls.env['social.media'].create({
            'name': 'Social Media',
        })
