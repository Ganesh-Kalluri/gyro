# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.addons.sale.tests.common import SaleCommon

class SaleManagementCommon(SaleCommon):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.empty_order_template = cls.env['sale.order.template'].create({
            'name': "Test Quotation Template",
        })
