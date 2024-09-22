# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class Track(models.Model):
    _inherit = 'event.track'

    def action_unschedule(self):
        self.ensure_one()
        self.date = None
        self.date_end = None
        return {'type': 'ir.actions.act_window_close'}
