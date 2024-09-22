# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'


    l10n_lt_official_social_security = fields.Char(string="Social Security Number")
