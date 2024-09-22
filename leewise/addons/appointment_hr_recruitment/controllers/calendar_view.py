# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.addons.appointment.controllers.calendar_view import AppointmentCalendarView
from leewise.http import request
from leewise.osv.expression import AND


class AppointmentHrRecruitmentCalendarView(AppointmentCalendarView):

    def _get_staff_user_appointment_invite_domain(self, appointment_type):
        domain = super()._get_staff_user_appointment_invite_domain(appointment_type)
        if 'default_applicant_id' in request.env.context:
            domain = AND([domain, [('applicant_id', '=', request.env.context['default_applicant_id'])]])
        return domain
