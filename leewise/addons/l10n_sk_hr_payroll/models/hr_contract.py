# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    l10n_sk_meal_voucher_employee = fields.Monetary("Meal Vouchers Amount (Employee)")
    l10n_sk_meal_voucher_employer = fields.Monetary("Meal Vouchers Amount (Employer)")
