# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    deferred_time_off_manager = fields.Many2one('res.users', related='company_id.deferred_time_off_manager', check_company=True, readonly=False)
