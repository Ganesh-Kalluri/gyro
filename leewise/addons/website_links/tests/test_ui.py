# Part of Leewise. See LICENSE file for full copyright and licensing details.

from unittest.mock import patch

import leewise.tests


@leewise.tests.common.tagged('post_install', '-at_install')
class TestUi(leewise.tests.HttpCase):

    def setUp(self):
        super().setUp()

        def _get_title_from_url(addr, **kw):
            return 'Contact Us | My Website'

        patcher = patch('leewise.addons.link_tracker.models.link_tracker.LinkTracker._get_title_from_url', wraps=_get_title_from_url)
        self.startPatcher(patcher)

    def test_01_test_ui(self):
        self.env['link.tracker'].search_or_create({
            'campaign_id': self.env['utm.campaign'].create({'name': 'Sale'}).id,
            'medium_id': self.env['utm.medium'].create({'name': 'Website'}).id,
            'source_id': self.env['utm.source'].create({'name': 'Search'}).id,
            'url': self.env["ir.config_parameter"].sudo().get_param("web.base.url") + '/contactus',
        })
        self.start_tour("/", 'website_links_tour', login="admin")
