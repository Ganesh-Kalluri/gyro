# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    deletion_delay = fields.Integer(config_parameter="documents.deletion_delay", default=30,
                                    help='Delay after permanent deletion of the document in the trash (days)')

    _sql_constraints = [
        ('check_deletion_delay', 'CHECK(deletion_delay >= 0)', 'The deletion delay should be positive.'),
    ]
