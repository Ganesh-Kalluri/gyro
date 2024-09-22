# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class FollowupLine(models.Model):
    _inherit = 'account_followup.followup.line'

    send_letter = fields.Boolean('Send a Letter', default=False)
