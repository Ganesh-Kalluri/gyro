# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details

from leewise import fields, models


class ReportProjectTaskUser(models.Model):
    _name = 'report.project.task.user.fsm'
    _inherit = 'report.project.task.user'
    _description = "FSM Tasks Analysis"
    _auto = False

    def _from(self):
        return super()._from() + """
                INNER JOIN project_project pp
                    ON pp.id = t.project_id
                    AND pp.is_fsm = 'true'
        """
