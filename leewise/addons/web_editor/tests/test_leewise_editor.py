# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

import leewise.tests

@leewise.tests.tagged("post_install", "-at_install")
class TestLeewiseEditor(leewise.tests.HttpCase):

    def test_leewise_editor_suite(self):
        self.browser_js('/web_editor/tests', "", "", login='admin', timeout=1800)
