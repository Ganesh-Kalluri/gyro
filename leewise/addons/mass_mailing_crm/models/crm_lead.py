# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _mailing_enabled = True
