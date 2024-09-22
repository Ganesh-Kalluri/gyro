# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class Partner(models.Model):
    _inherit = 'res.partner'
    _mailing_enabled = True
