# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class Groups(models.Model):
    _name = 'res.groups'
    _inherit = ['studio.mixin', 'res.groups']
