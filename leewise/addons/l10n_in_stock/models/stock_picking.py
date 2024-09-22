# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _should_generate_commercial_invoice(self):
        super(StockPicking, self)._should_generate_commercial_invoice()
        return True
