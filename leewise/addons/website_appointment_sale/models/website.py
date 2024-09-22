# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models
from leewise.osv import expression


class Website(models.Model):
    _inherit = 'website'

    def sale_product_domain(self):
        return expression.AND([
            super().sale_product_domain(),
            [('detailed_type', '!=', 'booking_fees')],
        ])
