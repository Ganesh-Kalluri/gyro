# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import fields, models


class AccountTaxGroup(models.Model):
    _inherit = 'account.tax.group'

    l10n_pe_edi_code = fields.Char('EDI Code', help="Peruvian EDI code to complement catalog 05")
