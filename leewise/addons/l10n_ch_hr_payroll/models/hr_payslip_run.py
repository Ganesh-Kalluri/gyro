# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class HrPayslipRun(models.Model):
    _inherit = 'hr.payslip.run'

    l10n_ch_pay_13th_month = fields.Boolean(
        string="Pay Thirteen Month")
