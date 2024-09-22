# -*- coding: utf-8 -*-
from leewise import fields, models


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_avatax_valid = fields.Boolean()