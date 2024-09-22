# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class IrDefault(models.Model):
    _name = 'ir.default'
    _inherit = ['studio.mixin', 'ir.default']
