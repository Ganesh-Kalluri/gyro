# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, fields


class HrEmployee(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    sign_request_ids = fields.Many2many(
        'sign.request', string='Requested Signatures')
    sign_request_count = fields.Integer(
        compute="_compute_sign_request_count",
        groups="hr_contract.group_hr_contract_manager",
    )

    def _compute_sign_request_count(self):
        for employee in self:
            contracts = self.env['hr.contract'].sudo().search([('employee_id', '=', employee.id)])
            sign_from_contract = contracts.mapped('sign_request_ids')

            sign_from_role = self.env['sign.request'].browse([])
            partner_ids = employee.user_id.partner_id | employee.work_contact_id
            if partner_ids:
                sign_from_role = self.env['sign.request.item'].search([
                    ('partner_id', 'in', partner_ids.ids),
                    ('role_id', '=', self.env.ref('sign.sign_item_role_employee').id)]).mapped('sign_request_id')

            employee.sign_request_count = len(set(sign_from_contract + sign_from_role + employee.sign_request_ids))

    def open_employee_sign_requests(self):
        self.ensure_one()
        contracts = self.env['hr.contract'].sudo().search([('employee_id', '=', self.id)])
        sign_from_contract = contracts.mapped('sign_request_ids')
        sign_from_role = self.env['sign.request']
        partner_ids = self.user_id.partner_id | self.work_contact_id
        if partner_ids:
            sign_from_role = self.env['sign.request.item'].search([
                ('partner_id', 'in', partner_ids.ids),
                ('role_id', '=', self.env.ref('sign.sign_item_role_employee').id)]).mapped('sign_request_id')
        sign_request_ids = sign_from_contract + sign_from_role + self.sign_request_ids
        if len(sign_request_ids.ids) == 1:
            return sign_request_ids.go_to_document()

        if self.env.user.has_group('sign.group_sign_user'):
            view_id = self.env.ref("sign.sign_request_view_kanban").id
        else:
            view_id = self.env.ref("hr_contract_sign.sign_request_employee_view_kanban").id

        return {
            'type': 'ir.actions.act_window',
            'name': 'Signature Requests',
            'view_mode': 'kanban,tree',
            'res_model': 'sign.request',
            'view_ids': [(view_id, 'kanban'), (False, 'tree')],
            'domain': [('id', 'in', sign_request_ids.ids)]
        }
