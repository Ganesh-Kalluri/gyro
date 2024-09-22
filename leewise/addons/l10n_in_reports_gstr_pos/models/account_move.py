# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_in_pos_session_ids = fields.One2many("pos.session", "move_id", "POS Sessions")