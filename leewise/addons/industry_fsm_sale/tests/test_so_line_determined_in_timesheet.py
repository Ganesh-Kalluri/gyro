# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import Command
from leewise.tests import tagged
from leewise.tools import float_round

from .common import TestFsmFlowSaleCommon


@tagged('-at_install', 'post_install')
class TestSoLineDeterminedInTimesheet(TestFsmFlowSaleCommon):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.fsm_so = cls.env['sale.order'].with_context(mail_notrack=True, mail_create_nolog=True).create({
            'partner_id': cls.partner_1.id,
            'partner_invoice_id': cls.partner_1.id,
            'partner_shipping_id': cls.partner_1.id,
            'order_line': [
                Command.create({
                    'name': cls.product_delivery_timesheet1.name,
                    'product_id': cls.product_delivery_timesheet1.id,
                    'product_uom_qty': 10,
                    'price_unit': cls.product_delivery_timesheet1.list_price,
                }),
                Command.create({
                    'product_id': cls.product_delivery_timesheet2.id,
                    'product_uom_qty': 5,
                    'price_unit': cls.product_delivery_timesheet2.list_price,
                }),
                Command.create({
                    'product_id': cls.product_delivery_timesheet3.id,
                    'product_uom_qty': 5,
                    'price_unit': cls.product_delivery_timesheet3.list_price,
                })
            ]
        })
        cls.fsm_so.action_confirm()

    def test_sol_determined_when_fsm_project_is_employee_rate(self):
        """ Test the SOL gives to the timesheet when the pricing_type in the fsm project is employee rate.

            Test Case:
            =========
            1) Create task with a SOL in the SO create in the setUpClass of this class,
            2) Create timesheet in the task and check if the SOL in the timesheet is the one in the task,
            3) Create timesheet in the task for the employee defined in the mapping and check if the SOL in this timesheet contains the service product and the price unit defined in the mapping for this employee.
            4) Create timesheet in the task for the employee defined in the mapping but no SOL in the SO linked to the task contains the service product defined in the mapping for this employee.
            5) Change the SOL in the task and check if only the SOL in the timesheet which does not concerne about the mapping changes.
            6) Add a mapping for the employee manager with a service product in the SOLs but with a different price unit.
                - Check if the timesheet of this employee manager does not change.
        """
        # 1) Create task with a SOL in the SO create in the setUpClass of this class
        task = self.env['project.task'].with_context({
            'mail_create_nolog': True,
            'default_project_id': self.fsm_project_employee_rate.id,
            'default_user_ids': self.project_user,
        }).create({
            'sale_line_id': self.fsm_so.order_line[:1].id,
            'name': 'Fsm Task',
        })

        # 2) Create timesheet in the task and check if the SOL in the timesheet is the one in the task
        employee_manager_timesheet = self.env['account.analytic.line'].create({
            'name': '/',
            'employee_id': self.employee_manager.id,
            'unit_amount': 1.0,
            'task_id': task.id,
            'project_id': self.fsm_project_employee_rate.id,
        })
        self.assertEqual(employee_manager_timesheet.so_line, task.sale_line_id, 'This timesheet should have the same SOL than the one in the task because the employee is not in the employee mappings.')
        self.assertEqual(task.sale_line_id.qty_delivered, 1.0, 'The quantity delivered should be equal to 1 for the SOL linked to the task.')

        # 3) Create timesheet in the task for the employee defined in the mapping and check if the SOL in this timesheet
        # contains the service product and the price unit defined in the mapping for this employee.
        employee_user3_timesheet = self.env['account.analytic.line'].create({
            'name': '/',
            'employee_id': self.employee_user3.id,
            'unit_amount': 2.0,
            'task_id': task.id,
            'project_id': self.fsm_project_employee_rate.id,
        })

        # Find the mapping for this employee
        employee_user3_mapping = self.fsm_project_employee_rate.sale_line_employee_ids.filtered(
            lambda mapping: mapping.employee_id == employee_user3_timesheet.employee_id
        )

        # Find the SOL containing the same product and price unit defined in the found mapping
        sol = self.fsm_so.order_line.filtered(
            lambda sol:
                sol.product_id == employee_user3_mapping.timesheet_product_id
                and sol.price_unit == employee_user3_mapping.price_unit
        )
        self.assertEqual(employee_user3_timesheet.so_line, sol, 'The SOL linked to the timesheet should be the one containing the service product with the same price unit defined for this employee in the mappings.')
        self.assertEqual(sol.qty_delivered, 2.0, 'The quantity delivered for this SOL should be the unit_amount of the timesheet, that is 2 hours.')

        # 4) Create timesheet in the task for the employee defined in the mapping but no SOL in the SO linked to the task
        # contains the service product defined in the mapping for this employee.
        employee_user_timesheet = self.env['account.analytic.line'].create({
            'name': '/',
            'employee_id': self.employee_user.id,
            'unit_amount': 3.0,
            'task_id': task.id,
            'project_id': self.fsm_project_employee_rate.id,
        })

        # Find the mapping for this employee
        employee_user_mapping = self.fsm_project_employee_rate.sale_line_employee_ids.filtered(
            lambda mapping: mapping.employee_id == employee_user_timesheet.employee_id
        )

        # Search if a SOL contains the same product and price unit defined in the found mapping
        self.assertFalse(
            any(
                sol.product_id == employee_user_mapping.timesheet_product_id and sol.price_unit == employee_user_mapping.price_unit
                for sol in self.fsm_so.order_line
            ),
            'No SOL contains the product and the same price unit than the mapping for this employee user.'
        )
        self.assertEqual(employee_user_timesheet.so_line, task.sale_line_id, 'The SOL of this timesheet should be the one in the task.')

        # 5) Change the SOL in the task and check if only the SOL in the timesheet which does not concerne about the mapping changes.
        sol = self.fsm_so.order_line.filtered(lambda sol: sol.product_id == self.product_delivery_timesheet3)[:1]
        task.write({
            'sale_line_id': sol.id,
        })
        self.assertTrue(task.sale_line_id == employee_manager_timesheet.so_line == sol, 'The SOL in the timesheet of employee manager should be the one defined in the task.')
        self.assertTrue(task.sale_line_id == employee_user_timesheet.so_line == sol, 'The SOL in the timesheet of employee user should also be the one defined in the task.')
        self.assertNotEqual(employee_user3_timesheet.so_line, task.sale_line_id, 'The SOL in the timesheet of employee user should remain the same than before and be not the one in the task.')

        # 6) Add a mapping for the employee manager with a service product in the SOLs but with a different price unit.
        mappings_count = len(self.fsm_project_employee_rate.sale_line_employee_ids)
        self.env['project.sale.line.employee.map'].create({
            'employee_id': self.employee_manager.id,
            'timesheet_product_id': self.product_order_timesheet1.id,
            'price_unit': 150,
            'project_id': self.fsm_project_employee_rate.id,
        })
        self.assertEqual(len(self.fsm_project_employee_rate.sale_line_employee_ids), mappings_count + 1, 'The mapping for the employee manager should added in the employee mappings.')

        # Check if the timesheet of the employee manager does not change.
        self.assertEqual(employee_manager_timesheet.so_line, task.sale_line_id, 'The timesheet of the employee manager keeps the same SOL than the one in the task because no SOL contains the same product with the same price unit defined in the mapping for this employee.')

    def test_fsm_sale_rounding(self):
        """
        Test rounding is correctly applied in the so line
        """
        self.task.write({'partner_id': self.partner_1.id})
        product_uom_qty = 0.333333
        quantity_precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
        # timesheet
        values = {
            'task_id': self.task.id,
            'project_id': self.task.project_id.id,
            'name': 'test timesheet',
            'user_id': self.env.uid,
            'unit_amount': product_uom_qty,
            'employee_id': self.employee_user2.id,
        }
        self.env['account.analytic.line'].create(values)

        # validation and SO
        self.task.with_user(self.project_user).action_fsm_validate()
        order = self.task.sale_order_id

        expected_price_subtotal = order.order_line.price_unit * float_round(product_uom_qty, precision_digits=quantity_precision)
        self.assertEqual(order.order_line.price_subtotal, expected_price_subtotal, "Order line subtotal is not correct")
