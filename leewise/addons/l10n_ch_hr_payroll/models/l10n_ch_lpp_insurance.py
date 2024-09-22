# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, fields


class l10nChLppInsurance(models.Model):
    _name = 'l10n.ch.lpp.insurance'
    _description = 'Swiss: LPP Insurances'

    name = fields.Char(required=True)
    customer_number = fields.Char(required=True)
    contract_number = fields.Char(required=True)
    insurance_company_address_id = fields.Many2one('res.partner')
    fund_number = fields.Char()
