# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.addons.l10n_in_hr_payroll.tests.common import TestPayrollCommon
from leewise.tests import tagged


@tagged('post_install_l10n', 'post_install', '-at_install')
class TestPaymentAdviceBatch(TestPayrollCommon):

    def test_00_payment_advice_batch_flow(self):
        # I want to generate a payslip from Payslip Batch.
        payslip_run = self.PayslipRun.create({
            'name': 'Payslip Batch'
        })

        # I create record for generating the Payslip for Payslip Batch.
        payslip_employee = self.PayslipEmployee.create({
            'employee_ids': [(4, self.rahul_emp.id)]
        })

        # I generate the payslip by clicking on Generate button wizard.
        payslip_employee.with_context(active_id=payslip_run.id).compute_sheet()

        # I check that the Payslip Batch is in "Draft"
        self.assertEqual(payslip_run.state, 'verify')

        # Now I close Payslip Batch
        payslip_run.write({'state': 'close'})

        # check that the Payslip Batch is "Close"
        self.assertEqual(payslip_run.state, 'close')

        # I create Advice from Payslip Batch using Create Advice button
        payslip_run.create_advice()

        # I check for Advice is created from Payslip Batch
        advice_ids = self.Advice.search([('batch_id', '=', payslip_run.id)])
        self.assertTrue(bool(advice_ids), "Advice is not created from Payslip Batch.")
