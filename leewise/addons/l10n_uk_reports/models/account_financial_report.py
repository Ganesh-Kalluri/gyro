# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import models, _


class BritishGenericTaxReportCustomHandler(models.AbstractModel):
    _name = 'l10n_uk.tax.report.handler'
    _inherit = 'account.tax.report.handler'
    _description = 'British Tax Report Custom Handler'

    def _custom_options_initializer(self, report, options, previous_options=None):
        super()._custom_options_initializer(report, options)
        # If token, but no refresh_token, check if you got the refresh_token on the server first
        # That way, you can see immediately if your login was successful after logging in
        # and the label of the button will be correct
        if self.env.user.l10n_uk_user_token and not self.env.user.l10n_uk_hmrc_vat_token:
            self.env['hmrc.service']._login()
        button_name = _('Send to HMRC') if self.env.user.l10n_uk_hmrc_vat_token else _('Connect to HMRC')
        options['buttons'].append({'name': button_name, 'action': 'send_hmrc', 'sequence': 50})

    def send_hmrc(self, options):
        # do the login if there is no token for the current user yet.
        if not self.env.user.l10n_uk_hmrc_vat_token and not options.get('_running_export_test'):
            return self.env['hmrc.service']._login()

        # Show wizard when sending to HMRC
        context = self.env.context.copy()
        context.update({'options': options})
        view_id = self.env.ref('l10n_uk_reports.hmrc_send_wizard_form').id
        return {'type': 'ir.actions.act_window',
                'name': _('Send to HMRC'),
                'res_model': 'l10n_uk.hmrc.send.wizard',
                'target': 'new',
                'view_mode': 'form',
                'views': [[view_id, 'form']],
                'context': context,
        }
