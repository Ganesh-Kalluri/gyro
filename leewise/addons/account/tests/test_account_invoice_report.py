# -*- coding: utf-8 -*-
from leewise.addons.account.tests.common import AccountTestInvoicingCommon
from leewise.tests import tagged
from leewise import fields


@tagged('post_install', '-at_install')
class TestAccountInvoiceReport(AccountTestInvoicingCommon):

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass(chart_template_ref=chart_template_ref)

        cls.invoices = cls.env['account.move'].create([
            {
                'move_type': 'out_invoice',
                'partner_id': cls.partner_a.id,
                'invoice_date': fields.Date.from_string('2016-01-01'),
                'currency_id': cls.currency_data['currency'].id,
                'invoice_line_ids': [
                    (0, None, {
                        'product_id': cls.product_a.id,
                        'quantity': 3,
                        'price_unit': 750,
                    }),
                    (0, None, {
                        'product_id': cls.product_a.id,
                        'quantity': 1,
                        'price_unit': 3000,
                    }),
                ]
            },
            {
                'move_type': 'out_receipt',
                'invoice_date': fields.Date.from_string('2016-01-01'),
                'currency_id': cls.currency_data['currency'].id,
                'invoice_line_ids': [
                    (0, None, {
                        'product_id': cls.product_a.id,
                        'quantity': 1,
                        'price_unit': 6000,
                    }),
                ]
            },
            {
                'move_type': 'out_refund',
                'partner_id': cls.partner_a.id,
                'invoice_date': fields.Date.from_string('2017-01-01'),
                'currency_id': cls.currency_data['currency'].id,
                'invoice_line_ids': [
                    (0, None, {
                        'product_id': cls.product_a.id,
                        'quantity': 1,
                        'price_unit': 1200,
                    }),
                ]
            },
            {
                'move_type': 'in_invoice',
                'partner_id': cls.partner_a.id,
                'invoice_date': fields.Date.from_string('2016-01-01'),
                'currency_id': cls.currency_data['currency'].id,
                'invoice_line_ids': [
                    (0, None, {
                        'product_id': cls.product_a.id,
                        'quantity': 1,
                        'price_unit': 60,
                    }),
                ]
            },
            {
                'move_type': 'in_receipt',
                'partner_id': cls.partner_a.id,
                'invoice_date': fields.Date.from_string('2016-01-01'),
                'currency_id': cls.currency_data['currency'].id,
                'invoice_line_ids': [
                    (0, None, {
                        'product_id': cls.product_a.id,
                        'quantity': 1,
                        'price_unit': 60,
                    }),
                ]
            },
            {
                'move_type': 'in_refund',
                'partner_id': cls.partner_a.id,
                'invoice_date': fields.Date.from_string('2017-01-01'),
                'currency_id': cls.currency_data['currency'].id,
                'invoice_line_ids': [
                    (0, None, {
                        'product_id': cls.product_a.id,
                        'quantity': 1,
                        'price_unit': 12,
                    }),
                ]
            },
        ])

    def assertInvoiceReportValues(self, expected_values_list):
        reports = self.env['account.invoice.report'].search([('company_id', '=', self.company_data['company'].id)], order='price_subtotal DESC, quantity ASC')
        expected_values_dict = [{
            'price_average': vals[0],
            'price_subtotal': vals[1],
            'quantity': vals[2],
            'price_margin': vals[3],
            'inventory_value': vals[4],
        } for vals in expected_values_list]

        self.assertRecordValues(reports, expected_values_dict)

    def test_invoice_report_multiple_types(self):
        self.assertInvoiceReportValues([
            # pylint: disable=bad-whitespace
            # price_average, price_subtotal, quantity, price_margin, inventory_value
            [          2000,           2000,        1,         1200,            -800], # price_unit = 6000, currency.rate = 3.0
            [          1000,           1000,        1,          200,            -800], # price_unit = 3000, currency.rate = 3.0
            [           250,            750,        3,        -1650,           -2400], # price_unit = 750,  currency.rate = 2.0
            [             6,              6,        1,            0,            -800], # price_unit = 12,   currency.rate = 2.0
            [            20,            -20,       -1,            0,             800], # price_unit = 60,   currency.rate = 3.0
            [            20,            -20,       -1,            0,             800], # price_unit = 60,   currency.rate = 3.0
            [           600,           -600,       -1,            0,             800], # price_unit = 1200, currency.rate = 2.0
        ])
