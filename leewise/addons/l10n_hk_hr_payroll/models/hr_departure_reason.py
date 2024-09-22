# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class DepartureReason(models.Model):
    _inherit = "hr.departure.reason"

    l10n_hk_ir56f_code = fields.Char()
