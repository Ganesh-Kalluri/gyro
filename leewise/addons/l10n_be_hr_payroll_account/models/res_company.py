# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    exemption_doctor_master_account_id = fields.Many2one('account.account', check_company=True)
    exemption_bachelor_account_id = fields.Many2one('account.account', check_company=True)
    exemption_bachelor_capping_account_id = fields.Many2one('account.account', check_company=True)
    exemption_journal_id = fields.Many2one('account.journal', 'Salary Journal', check_company=True)
