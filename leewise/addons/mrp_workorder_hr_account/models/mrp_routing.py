# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class MrpRouting(models.Model):
    _inherit = 'mrp.routing.workcenter'

    def _total_cost_per_hour(self):
        return super()._total_cost_per_hour() + self.workcenter_id.employee_costs_hour * self.employee_ratio
