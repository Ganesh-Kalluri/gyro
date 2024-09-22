# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import models

class PosOrder(models.Model):
    _inherit = 'pos.order'

    def _send_order(self):
        super()._send_order()
        self.env['pos_preparation_display.order'].sudo().process_order(self.id)
