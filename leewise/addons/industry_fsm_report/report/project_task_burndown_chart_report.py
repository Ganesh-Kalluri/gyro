# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models

class ReportProjectTaskBurndownChart(models.AbstractModel):
    _inherit = 'project.task.burndown.chart.report'

    worksheet_template_id = fields.Many2one('worksheet.template', string="Worksheet Template", readonly=True)

    @property
    def task_specific_fields(self):
        return super().task_specific_fields + [
            'worksheet_template_id',
        ]
