# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class IrFilters(models.Model):
    _name = 'ir.filters'
    _inherit = ['studio.mixin', 'ir.filters']
