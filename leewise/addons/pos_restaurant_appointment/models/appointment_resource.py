# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import fields, models

class AppointmentResource(models.Model):
    _inherit = 'appointment.resource'

    # this should be one2one
    pos_table_ids = fields.One2many('restaurant.table', 'appointment_resource_id', string='POS Table')
