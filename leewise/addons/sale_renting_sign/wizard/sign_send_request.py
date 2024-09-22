# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import fields, models


class SignSendRequest(models.TransientModel):
    _inherit = "sign.send.request"

    sale_order_id = fields.Many2one("sale.order", string="Sales Order")

    def create_request(self):
        sign_request = super(SignSendRequest, self).create_request()
        if self.sale_order_id:
            sign_request.sale_order_id = self.sale_order_id
        return sign_request
