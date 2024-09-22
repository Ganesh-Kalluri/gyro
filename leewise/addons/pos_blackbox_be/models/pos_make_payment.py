# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models
from leewise.exceptions import UserError
from leewise.tools.translate import _


class PosMakePayment(models.TransientModel):
    _inherit = "pos.make.payment"

    def check(self):
        order = self.env["pos.order"].browse(self.env.context.get("active_id"))

        if order.config_id.iface_fiscal_data_module:
            raise UserError(
                _("Adding additional payments to registered orders is not allowed.")
            )

        return super().check()
