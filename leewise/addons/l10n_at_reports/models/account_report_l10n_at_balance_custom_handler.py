# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2023 WT-IO-IT GmbH (https://www.wt-io-it.at)
#                    Mag. Wolfgang Taferner <wolfgang.taferner@wt-io-it.at>
from leewise import models, _
from leewise.tools import float_compare

class AccountReportCustomHandler(models.AbstractModel):
    _name = 'account.report.l10n_at.balance.custom.handler'
    _inherit = 'account.report.custom.handler'
    _description = 'Austrian Balance Sheet Report Custom Handler'

    def _custom_line_postprocessor(self, report, options, lines, warnings=None):
        """ Postprocesses the result of the report's _get_lines() before returning it. """
        equity_root = self.env.ref('l10n_at_reports.account_financial_report_l10n_at_paragraph_224_ugb_line_passiva_1', raise_if_not_found=False)
        for line in lines:
            _model, res_id = report._get_model_info_from_id(line['id'])
            if equity_root and equity_root.id == res_id:
                for column in line['columns']:
                    if column['expression_label'] == 'balance':
                        if float_compare(column['no_format'], 0, 2) < 0:
                            line['name'] = _("A. Negative equity capital")
        return lines
