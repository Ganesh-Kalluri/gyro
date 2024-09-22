# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from unittest.mock import patch

import leewise.tests
from leewise.addons.pos_self_order.tests.self_order_common_test import SelfOrderCommonTest
# from leewise.addons.pos_online_payment.models.pos_payment_method import PosPaymentMethod


@leewise.tests.tagged("post_install", "-at_install")
class TestSelfOrderFrontendMobile(SelfOrderCommonTest):
    pass
