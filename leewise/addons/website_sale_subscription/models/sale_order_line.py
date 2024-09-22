# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _is_reorder_allowed(self):
        if self.recurring_invoice:
            return False
        return super(SaleOrderLine, self)._is_reorder_allowed()
