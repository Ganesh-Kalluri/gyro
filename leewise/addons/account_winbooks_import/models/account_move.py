# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # technical field used to reconcile the journal items in Leewise as they were in Winbooks
    winbooks_matching_number = fields.Char(help="Matching number that was used in Winbooks")  # DEPRECATED in 17.0
    winbooks_line_id = fields.Char(help="Line ID that was used in Winbooks")
