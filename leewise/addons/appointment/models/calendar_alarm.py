# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class Alarm(models.Model):
    _inherit = "calendar.alarm"

    default_for_new_appointment_type = fields.Boolean(
        "New Appointments Default", help="Use as default for new Appointment Types")
