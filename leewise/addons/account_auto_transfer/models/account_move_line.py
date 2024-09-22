# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, models, _
from leewise.exceptions import UserError


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.constrains('tax_ids')
    def _check_auto_transfer_line_ids_tax(self):
        if any(line.move_id.transfer_model_id and line.tax_ids for line in self):
            raise UserError(_("You cannot set Tax on Automatic Transfer's entries."))
