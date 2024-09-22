# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    ldaps = fields.One2many('res.company.ldap', 'company', string='LDAP Parameters',
                               copy=True, groups="base.group_system")
