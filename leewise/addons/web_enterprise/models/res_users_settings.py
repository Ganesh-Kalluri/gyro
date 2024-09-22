# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResUsersSettings(models.Model):
    _inherit = 'res.users.settings'

    homemenu_config = fields.Json(string="Home Menu Configuration", readonly=True)
