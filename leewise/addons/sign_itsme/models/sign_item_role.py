# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models

class SignItemParty(models.Model):
    _inherit = "sign.item.role"

    auth_method = fields.Selection(selection_add=[
        ('itsme', 'Via itsme®')
    ], ondelete={'itsme': 'cascade'})
