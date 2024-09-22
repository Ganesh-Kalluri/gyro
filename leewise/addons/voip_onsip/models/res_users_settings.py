# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResUsersSettings(models.Model):
    _inherit = "res.users.settings"

    onsip_auth_username = fields.Char("OnSIP Auth Username")
