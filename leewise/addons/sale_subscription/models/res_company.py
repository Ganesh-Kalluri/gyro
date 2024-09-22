# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    # Default subscription parameters
    subscription_default_plan_id = fields.Many2one('sale.subscription.plan', string='Default Recurrence')
