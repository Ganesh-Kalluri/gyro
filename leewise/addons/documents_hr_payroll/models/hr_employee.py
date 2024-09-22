# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    documents_share_id = fields.Many2one(groups="hr_payroll.group_hr_payroll_user")
