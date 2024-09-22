# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class Company(models.Model):
    _inherit = "res.company"

    check_account_audit_trail = fields.Boolean(string='Audit Trail')
