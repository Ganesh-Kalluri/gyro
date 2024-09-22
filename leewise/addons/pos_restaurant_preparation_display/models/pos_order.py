# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, api


class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def _get_line_note(self, line):
        return line.note
