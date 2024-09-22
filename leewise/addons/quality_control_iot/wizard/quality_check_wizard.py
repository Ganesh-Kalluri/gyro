# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class QualityCheckWizard(models.TransientModel):

    _inherit = 'quality.check.wizard'

    ip = fields.Char(related='current_check_id.ip')
    identifier = fields.Char(related='current_check_id.identifier')
