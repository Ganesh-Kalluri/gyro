# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class GamificationBadge(models.Model):
    _name = 'gamification.badge'
    _inherit = ['gamification.badge', 'website.published.mixin']
