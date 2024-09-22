# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class MailTemplate(models.Model):
    _name = 'mail.template'
    _description = 'Email Templates'
    _inherit = ['studio.mixin', 'mail.template']
