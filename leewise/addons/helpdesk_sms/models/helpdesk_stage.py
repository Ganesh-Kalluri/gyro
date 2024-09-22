# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class HelpdeskStage(models.Model):
    _inherit = "helpdesk.stage"

    sms_template_id = fields.Many2one('sms.template', string="SMS Template",
        domain=[('model', '=', 'helpdesk.ticket')], help="SMS automatically sent to the customer when the ticket reaches this stage.")
