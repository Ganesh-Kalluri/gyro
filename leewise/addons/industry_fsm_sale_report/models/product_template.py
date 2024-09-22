# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models, api
from leewise.tools.sql import column_exists, create_column


class ProductTemplate(models.Model):
    _inherit = "product.template"

    allow_worksheets = fields.Boolean(related='project_id.allow_worksheets', readonly=True)
    worksheet_template_id = fields.Many2one(
        'worksheet.template', string="Worksheet Template", company_dependent=True, domain="[('res_model', '=', 'project.task')]")

    def _compute_worksheet_template_id(self, keep_template=False):
        for template in self:
            if not template.allow_worksheets or template.service_tracking not in ['task_global_project', 'task_new_project'] or not template.project_id.is_fsm:
                template.worksheet_template_id = False
            else:
                # Keep the old template if `keep_template` is true, this only applies if the template would have been non 0
                old_template = template.worksheet_template_id if keep_template else False
                template.worksheet_template_id = old_template or template.project_id.worksheet_template_id

    @api.model_create_multi
    def create(self, create_vals):
        res = super().create(create_vals)
        res.filtered(lambda t: not t.worksheet_template_id)._compute_worksheet_template_id()
        return res

    def write(self, vals):
        res = super().write(vals)
        if ('service_tracking' in vals or 'project_id' in vals):
            self._compute_worksheet_template_id(keep_template=('worksheet_template_id' in vals))
        return res
