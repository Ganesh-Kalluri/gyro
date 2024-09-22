# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResCountry(models.Model):
    _inherit = 'res.country'

    intrastat = fields.Boolean(string='Intrastat member')
