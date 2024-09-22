# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['mail.thread.phone', 'res.partner']
