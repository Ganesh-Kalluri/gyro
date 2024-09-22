# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class HrContractSalaryResume(models.Model):
    _inherit = 'hr.contract.salary.resume'

    def _get_available_fields(self):
        result = super()._get_available_fields()
        return list(set(result + [('monthly_benefit', 'Nature'),
                         ('monthly_cash', 'Monthly Cash'),
                         ('yearly_cash', 'Yearly Cash'),
                         ('annual_time_off', 'Annual Time Off'),
                         ('holidays', 'Extra Time Off'),
                         ('SALARY', 'Salary')]))

    code = fields.Selection(_get_available_fields)
