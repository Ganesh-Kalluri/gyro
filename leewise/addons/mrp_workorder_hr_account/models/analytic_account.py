# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class AccountAnalyticAccountLine(models.Model):
    _inherit = 'account.analytic.line'

    employee_id = fields.Many2one('hr.employee', "Employee")
