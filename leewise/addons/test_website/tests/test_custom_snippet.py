# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

import leewise.tests
from leewise.tools import mute_logger


@leewise.tests.common.tagged('post_install', '-at_install')
class TestCustomSnippet(leewise.tests.HttpCase):

    @mute_logger('leewise.addons.http_routing.models.ir_http', 'leewise.http')
    def test_01_run_tour(self):
        self.start_tour(self.env['website'].get_client_action_url('/'), 'test_custom_snippet', login="admin")
