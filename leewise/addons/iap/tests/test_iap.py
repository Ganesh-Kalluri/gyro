# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.tests.common import TransactionCase


class TestIAP(TransactionCase):
    def test_get_account(self):
        account = self.env["iap.account"].get("random_service_name")
        self.assertTrue(account.account_token, "Must be able to read the field")
