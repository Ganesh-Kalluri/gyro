# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from . import models


def _create_livechat_channel(env):
    env['helpdesk.team'].search([('use_website_helpdesk_livechat', '=', True)])._create_livechat_channel()
