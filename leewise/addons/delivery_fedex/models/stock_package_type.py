# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import fields, models


class PackageType(models.Model):
    _inherit = 'stock.package.type'

    package_carrier_type = fields.Selection(selection_add=[('fedex', 'FedEx')])
