# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    @api.model
    def winbooks_import_action(self):
        return self.env["ir.actions.actions"]._for_xml_id("account_winbooks_import.winbooks_import_action")
