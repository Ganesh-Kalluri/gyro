# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details

from leewise.tests import tagged

from .test_sale_planning import TestCommonSalePlanning
from leewise.addons.planning.tests.test_ui_common import TestUiCommon

@tagged('post_install', '-at_install')
class TestSalePlanningUi(TestCommonSalePlanning, TestUiCommon):

    def test_01_ui_inherit(self):
        self.plannable_so.action_confirm()
        self.start_tour("/", 'sale_planning_test_tour', login='admin')
