# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, fields, models, _
from leewise.exceptions import UserError
from leewise.osv import expression


class AccountPaymentMethodLine(models.Model):
    _inherit = "account.payment.method.line"

    payment_provider_id = fields.Many2one(
        comodel_name='payment.provider',
        compute='_compute_payment_provider_id',
        store=True
    )
    payment_provider_state = fields.Selection(
        related='payment_provider_id.state'
    )

    @api.depends('payment_method_id')
    def _compute_payment_provider_id(self):
        providers = self.env['payment.provider'].sudo().search([
            *self.env['payment.provider']._check_company_domain(self.journal_id.company_id),
            ('code', 'in', self.mapped('code')),
        ])

        # Make sure to pick the active provider, if any.
        providers_map = dict()
        for provider in providers:
            current_value = providers_map.get((provider.code, provider.company_id), False)
            if current_value and current_value.state != 'disabled':
                continue

            providers_map[(provider.code, provider.company_id)] = provider

        for line in self:
            code = line.payment_method_id.code
            company = line.journal_id.company_id
            line.payment_provider_id = False
            while not line.payment_provider_id and company:
                line.payment_provider_id = providers_map.get((code, company), False)
                company = company.parent_id

    @api.model
    def _get_payment_method_domain(self, code):
        # OVERRIDE
        domain = super()._get_payment_method_domain(code)
        information = self._get_payment_method_information().get(code)

        unique = information.get('mode') == 'unique'
        if unique:
            company_ids = self.env['payment.provider'].sudo().search([('code', '=', code)]).mapped('company_id')
            if company_ids:
                domain = expression.AND([domain, self.env['payment.provider']._check_company_domain(company_ids)])

        return domain

    @api.ondelete(at_uninstall=False)
    def _unlink_except_active_provider(self):
        """ Ensure we don't remove an account.payment.method.line that is linked to a provider
        in the test or enabled state.
        """
        active_provider = self.payment_provider_id.filtered(lambda provider: provider.state in ['enabled', 'test'])
        if active_provider:
            raise UserError(_(
                "You can't delete a payment method that is linked to a provider in the enabled "
                "or test state.\n""Linked providers(s): %s",
                ', '.join(a.display_name for a in active_provider),
            ))

    def action_open_provider_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Provider'),
            'view_mode': 'form',
            'res_model': 'payment.provider',
            'target': 'current',
            'res_id': self.payment_provider_id.id
        }
