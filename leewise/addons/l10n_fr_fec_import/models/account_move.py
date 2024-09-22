# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    fec_matching_number = fields.Char(help="Matching code that is used in FEC import for reconciliation")  # DEPRECATED in 17.0
