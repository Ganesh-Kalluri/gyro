# coding: utf-8
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_social_demo = fields.Boolean('Enable Demo Mode', groups="base.group_system")
