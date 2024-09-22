# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

import leewise
from leewise.tests import tagged
from leewise.tests.common import HttpCase


@tagged('post_install', '-at_install')
class TestSpreadsheetTemplate(HttpCase):

    def test_insert_pivot_in_spreadsheet(self):
        self.env['crm.lead'].create({
            'name': 'Test Lead',
            'user_id': self.env.ref('base.user_admin').id,
        })
        self.start_tour('/web', 'insert_crm_pivot_in_spreadsheet', login='admin')
