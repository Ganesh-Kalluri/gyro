# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models

class PlanningRole(models.Model):
    _inherit = 'planning.role'

    product_ids = fields.One2many('product.template', 'planning_role_id', string='Services', domain=[('type', '=', 'service'), ('sale_ok', '=', True)])
