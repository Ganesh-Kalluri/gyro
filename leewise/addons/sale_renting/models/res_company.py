# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    # RENTAL company defaults :

    # Extra Costs

    extra_hour = fields.Float("Per Hour", default=0.0)
    extra_day = fields.Float("Per Day", default=0.0)
    min_extra_hour = fields.Integer("Minimum delay time before applying fines.", default=2)

    extra_product = fields.Many2one(
        'product.product', string="Product",
        help="The product is used to add the cost to the sales order",
        domain="[('type', '=', 'service')]")

    _sql_constraints = [
        ('min_extra_hour',
            "CHECK(min_extra_hour >= 1)",
            "Minimal delay time before applying fines has to be positive."),
    ]
