# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class AccountTaxReportActivityType(models.Model):
    _inherit = "mail.activity.type"

    category = fields.Selection(selection_add=[('tax_report', 'Tax report')])
