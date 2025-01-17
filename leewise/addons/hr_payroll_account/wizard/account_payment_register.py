# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, _


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    def _create_payments(self):
        payments = super()._create_payments()
        if self.env.context.get('hr_payroll_payment_register'):
            payslip = self.env['hr.payslip'].browse(self.env.context['hr_payroll_payment_register'])
            for payment in payments:
                payment.message_post_with_source(
                    'mail.message_origin_link',
                    render_values={'self': payment, 'origin': payslip},
                    subtype_xmlid='mail.mt_note',
                )
                payslip.message_post(body=_("Payment done at %s", payment._get_html_link()))
        return payments

    def _reconcile_payments(self, to_process, edit_mode=False):
        res = super()._reconcile_payments(to_process, edit_mode=edit_mode)
        if self.env.context.get('hr_payroll_payment_register'):
            payslip = self.env['hr.payslip'].browse(self.env.context['hr_payroll_payment_register'])
            if all(line.currency_id.is_zero(line.amount_residual_currency) for line in payslip.move_id.line_ids):
                payslip.write({
                    "state": "paid",
                    "paid_date": self.payment_date
                })
        return res
