# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models
from leewise.osv import expression

class SaleOrder(models.Model):
    _inherit = "sale.order"
    _mailing_enabled = True

    def _mailing_get_default_domain(self, mailing):
        domain = super()._mailing_get_default_domain(mailing)
        return expression.AND([domain, [('subscription_state', '=', '3_progress')]])
