# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    check_ids = fields.One2many('quality.check', domain=[('workorder_id', '=', False)])
