# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import fields, models


class ProductPackaging(models.Model):
    _inherit = 'stock.package.type'

    package_carrier_type = fields.Selection(selection_add=[('ups_rest', 'UPS')])
