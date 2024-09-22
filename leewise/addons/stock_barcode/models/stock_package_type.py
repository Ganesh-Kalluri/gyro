# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, models


class PackageType(models.Model):
    _inherit = 'stock.package.type'

    @api.model
    def _get_fields_stock_barcode(self):
        return ['barcode', 'name']
