# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models

class ContractHistory(models.Model):
    _inherit = 'hr.contract.history'

    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account', readonly=True)
