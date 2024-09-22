# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    account_edi_proxy_client_ids = fields.One2many('account_edi_proxy_client.user', inverse_name='company_id')
