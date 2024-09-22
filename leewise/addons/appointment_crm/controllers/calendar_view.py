# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.addons.appointment.controllers.calendar_view import AppointmentCalendarView
from leewise.http import request
from leewise.osv.expression import AND


class AppointmentCrmCalendarView(AppointmentCalendarView):

    def _get_staff_user_appointment_invite_domain(self, appointment_type):
        domain = super()._get_staff_user_appointment_invite_domain(appointment_type)
        if 'default_opportunity_id' in request.env.context:
            domain = AND([domain, [('opportunity_id', '=', request.env.context['default_opportunity_id'])]])
        return domain
