# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class StockLandedCost(models.Model):
    _inherit = 'stock.landed.cost'

    company_id = fields.Many2one('res.company', 'Company', required=True, related=False, default=lambda self: self.env.company)
