# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models

class User(models.Model):
    _inherit = 'res.users'

    # -----------------------------------------
    # Business Methods
    # -----------------------------------------

    def _get_project_task_resource(self):
        return self.employee_id.resource_id
