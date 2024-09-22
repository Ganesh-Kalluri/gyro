# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, fields, models


class View(models.Model):
    _inherit = 'ir.ui.view'

    type = fields.Selection(selection_add=[('grid', "Grid")])
