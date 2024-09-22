# Part of Leewise. See LICENSE file for full copyright and licensing details.
# -*- coding: utf-8 -*-

import leewise.tests


@leewise.tests.tagged('post_install', '-at_install')
class TestUi(leewise.tests.HttpCase):
    def test_ui(self):
        self.start_tour("/web", 'helpdesk_tour', login="admin")
