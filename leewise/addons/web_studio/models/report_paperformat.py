# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class ReportPaperformat(models.Model):
    _name = 'report.paperformat'
    _inherit = ['studio.mixin', 'report.paperformat']
