# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from collections import defaultdict

from leewise import _, api, fields, models
from leewise.tools import float_round


class ProductProduct(models.Model):
    _inherit = 'product.product'

    fsm_quantity = fields.Float('Material Quantity', compute="_compute_fsm_quantity", inverse="_inverse_fsm_quantity", search="_search_fsm_quantity")
    fsm_partner_price = fields.Float('Partner Price', compute="_compute_fsm_partner_price")
    fsm_partner_price_currency_id = fields.Many2one('res.currency', compute="_compute_fsm_partner_price")

    @api.depends_context('fsm_task_id')
    @api.depends('fsm_quantity')
    def _compute_fsm_partner_price(self):
        task = self._get_contextual_fsm_task()
        price_per_product = {}
        product_per_quantity = defaultdict(lambda: self.env['product.product'])
        for product in self:
            product_per_quantity[product.fsm_quantity] |= product
        for quantity, products in product_per_quantity.items():
            price_per_product = {**price_per_product, **task.pricelist_id._get_products_price(products, quantity)}
        for product in self:
            product.fsm_partner_price = price_per_product.get(product.id, product.list_price)
            product.fsm_partner_price_currency_id = task.currency_id or product.currency_id

    @api.depends_context('fsm_task_id')
    def _compute_fsm_quantity(self):
        task = self._get_contextual_fsm_task()
        if task:

            SaleOrderLine = self.env['sale.order.line']
            if self.user_has_groups('project.group_project_user'):
                task = task.sudo()
                SaleOrderLine = SaleOrderLine.sudo()

            products_qties = SaleOrderLine._read_group(
                [('id', 'in', task.sale_order_id.order_line.ids), ('task_id', '=', task.id), ('product_id', '!=', False)],
                ['product_id'], ['product_uom_qty:sum'])
            qty_dict = {product.id: product_uom_qty_sum for product, product_uom_qty_sum in products_qties}
            for product in self:
                product.fsm_quantity = qty_dict.get(product.id, 0)
        else:
            self.fsm_quantity = False

    def _inverse_fsm_quantity(self):
        task = self._get_contextual_fsm_task()
        if task:
            SaleOrderLine_sudo = self.env['sale.order.line'].sudo()
            sale_lines_read_group = SaleOrderLine_sudo._read_group([
                ('order_id', '=', task.sale_order_id.id),
                ('product_id', 'in', self.ids),
                ('task_id', '=', task.id)],
                ['product_id', 'sequence'],
                ['id:array_agg'])
            sale_lines_per_product = defaultdict(lambda: self.env['sale.order.line'])
            for product, __, ids in sale_lines_read_group:
                sale_lines_per_product[product.id] |= SaleOrderLine_sudo.browse(ids)
            for product in self:
                sale_lines = sale_lines_per_product.get(product.id, self.env['sale.order.line'])
                all_editable_lines = sale_lines.filtered(lambda l: l.qty_delivered == 0 or l.qty_delivered_method == 'manual' or not l.order_id.locked)
                diff_qty = product.fsm_quantity - sum(sale_lines.mapped('product_uom_qty'))
                if all_editable_lines:  # existing line: change ordered qty (and delivered, if delivered method)
                    if diff_qty > 0:
                        vals = {
                            'product_uom_qty': all_editable_lines[0].product_uom_qty + diff_qty,
                        }
                        if product.service_type == 'manual':
                            vals['qty_delivered'] = all_editable_lines[0].product_uom_qty + diff_qty
                        all_editable_lines[0].with_context(fsm_no_message_post=True).write(vals)
                        continue
                    # diff_qty is negative, we remove the quantities from existing editable lines:
                    for line in all_editable_lines:
                        new_line_qty = max(0, line.product_uom_qty + diff_qty)
                        diff_qty += line.product_uom_qty - new_line_qty
                        if product.service_type == 'manual':
                            line.with_context(fsm_no_message_post=True).qty_delivered = new_line_qty
                        line.with_context(fsm_no_message_post=True).product_uom_qty = new_line_qty
                        if diff_qty == 0:
                            break
                elif diff_qty > 0:  # create new SOL
                    vals = {
                        'order_id': task.sale_order_id.id,
                        'product_id': product.id,
                        'product_uom_qty': diff_qty,
                        'product_uom': product.uom_id.id,
                        'task_id': task.id
                    }
                    if product.service_type == 'manual':
                        vals['qty_delivered'] = diff_qty

                    sol_sudo = SaleOrderLine_sudo.create(vals)
                    if task.sale_order_id.pricelist_id.discount_policy != 'without_discount':
                        sol_sudo.discount = 0.0

    @api.model
    def _search_fsm_quantity(self, operator, value):
        if not (isinstance(value, int) or (isinstance(value, bool) and value is False)):
            raise ValueError(_('Invalid value: %s', value))
        if operator not in ('=', '!=', '<=', '<', '>', '>=') or (operator == '!=' and value is False):
            raise ValueError(_('Invalid operator: %s', operator))

        task = self._get_contextual_fsm_task()
        if not task:
            return []
        op = 'inselect'
        if value is False:
            value = 0
            operator = '>='
            op = 'not inselect'
        query = """
            SELECT sol.product_id
              FROM sale_order_line sol
         LEFT JOIN sale_order so
                ON sol.order_id = so.id
         LEFT JOIN project_task task
                ON so.id = task.sale_order_id
             WHERE task.id = %s
               AND sol.product_uom_qty {} %s
        """.format(operator)
        return [('id', op, (query, (task.id, value)))]

    @api.model
    def _get_contextual_fsm_task(self):
        task_id = self.env.context.get('fsm_task_id')
        if task_id:
            return self.env['project.task'].browse(task_id)
        return self.env['project.task']

    def set_fsm_quantity(self, quantity):
        task = self._get_contextual_fsm_task()
        # project user with no sale rights should be able to change material quantities
        if not task or quantity and quantity < 0 or not self.user_has_groups('project.group_project_user'):
            return
        self = self.sudo()

        # don't add material on locked SO
        if task.sale_order_id.sudo().locked:
            return False
        # ensure that the task is linked to a sale order
        task._fsm_ensure_sale_order()
        wizard_product_lot = self.action_assign_serial(from_onchange=True)
        if wizard_product_lot:
            return wizard_product_lot
        self.fsm_quantity = float_round(quantity or 0, precision_rounding=self.uom_id.rounding)
        return True

    # Is override by fsm_stock to manage lot
    def action_assign_serial(self, from_onchange=False):
        return False

    def fsm_add_quantity(self):
        return self.set_fsm_quantity(self.sudo().fsm_quantity + 1)

    def fsm_remove_quantity(self):
        fsm_product_qty = self.sudo().fsm_quantity
        fsm_product_qty = fsm_product_qty - 1 if fsm_product_qty > 1 else 0
        return self.set_fsm_quantity(fsm_product_qty)
