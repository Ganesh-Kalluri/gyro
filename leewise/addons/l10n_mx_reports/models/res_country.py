# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class Country(models.Model):
    _inherit = 'res.country'

    demonym = fields.Char(translate=True, help="Adjective for relationship"
                          " between a person and a country.")
