# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, fields


class Department(models.Model):
    _inherit = 'hr.department'

    # Get department name using superuser, because model is not accessible for portal users
    display_name = fields.Char(compute='_compute_display_name', compute_sudo=True)
