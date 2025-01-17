# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, fields, _

class SaveSpreadsheetTemplate(models.TransientModel):
    _name = 'save.spreadsheet.template'
    _inherit = "spreadsheet.mixin"
    _description= "Spreadsheet Template Save Wizard"

    template_name = fields.Char(required=True)

    def save_template(self):
        self.ensure_one()
        self.env['spreadsheet.template'].create({
            'name': self.template_name,
            'spreadsheet_data': self.spreadsheet_data,
            'thumbnail': self.thumbnail,
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': _('"%s" saved as template', self.template_name),
                'sticky': False,
                'type': 'info',
            }
        }
