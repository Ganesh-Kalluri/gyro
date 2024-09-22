# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models
from leewise.exceptions import UserError
from leewise.tools.translate import _


class Module(models.Model):
    _inherit = "ir.module.module"

    def module_uninstall(self):
        for module_to_remove in self:
            if module_to_remove.name == "pos_blackbox_be":
                raise UserError(_("This module is not allowed to be removed."))

        return super().module_uninstall()
