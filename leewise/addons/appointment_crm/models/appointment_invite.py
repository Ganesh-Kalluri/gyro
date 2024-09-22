# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class AppointmentInviteCrm(models.Model):
    _inherit = "appointment.invite"

    opportunity_id = fields.Many2one('crm.lead', "Opportunity/Lead",
        help="Link an opportunity/lead to the appointment invite created.\n"
            "Used when creating an invitation from the Meeting action in the crm form view.")
