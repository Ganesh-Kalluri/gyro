# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, models


class ProjectTaskRecurrence(models.Model):
    _inherit = 'project.task.recurrence'

    @api.model
    def _get_recurring_fields_to_copy(self):
        return ['worksheet_template_id'] + super()._get_recurring_fields_to_copy()
