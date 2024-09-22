# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def action_website_test_setting(self):
        return self.env['website'].get_client_action('/')
