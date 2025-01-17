# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    documents_spreadsheet_folder_id = fields.Many2one(
        'documents.folder', related='company_id.documents_spreadsheet_folder_id', readonly=False)
