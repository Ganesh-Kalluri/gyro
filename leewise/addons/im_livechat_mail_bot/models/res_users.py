# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, fields


class Users(models.Model):
    _inherit = 'res.users'

    leewisebot_state = fields.Selection(selection_add=[
        ('onboarding_canned', 'Onboarding canned'),
    ], ondelete={'onboarding_canned': lambda users: users.write({'leewisebot_state': 'disabled'})})
