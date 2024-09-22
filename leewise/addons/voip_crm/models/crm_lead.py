# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class CrmLead(models.Model):
    _name = "crm.lead"
    _inherit = ["crm.lead", "voip.queue.mixin"]
