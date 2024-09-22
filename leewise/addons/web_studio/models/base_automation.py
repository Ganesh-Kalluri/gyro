# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class BaseAutomation(models.Model):
    _name = 'base.automation'
    _inherit = ['studio.mixin', 'base.automation']
