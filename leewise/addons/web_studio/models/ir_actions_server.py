# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class IrActionsServer(models.Model):
    _name = 'ir.actions.server'
    _inherit = ['studio.mixin', 'ir.actions.server']
