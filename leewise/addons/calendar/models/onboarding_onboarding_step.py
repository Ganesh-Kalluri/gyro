# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, models


class OnboardingStep(models.Model):
    _inherit = 'onboarding.onboarding.step'

    @api.model
    def action_view_start_calendar_sync(self):
        action = self.env["ir.actions.actions"]._for_xml_id("calendar.action_view_start_calendar_sync")
        return action
