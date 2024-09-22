# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _is_purchase_return(self):
        res = super()._is_purchase_return()
        return res or self._is_subcontract_return()