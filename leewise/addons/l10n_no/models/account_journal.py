# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    invoice_reference_model = fields.Selection(selection_add=[
        ('no', 'Norway')
    ], ondelete={'no': lambda recs: recs.write({'invoice_reference_model': 'leewise'})})
