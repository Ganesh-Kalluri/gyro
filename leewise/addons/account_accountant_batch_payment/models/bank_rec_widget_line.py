# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class BankRecWidgetLine(models.Model):
    _inherit = 'bank.rec.widget.line'

    source_batch_payment_id = fields.Many2one(comodel_name='account.batch.payment')
