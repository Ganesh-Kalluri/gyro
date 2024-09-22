# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    def _get_kitchen_printer(self):
        res = super()._get_kitchen_printer()
        for printer in self.printer_ids:
            if printer.device_identifier:
                res[printer.id]["device_identifier"] = printer.device_identifier
        return res
