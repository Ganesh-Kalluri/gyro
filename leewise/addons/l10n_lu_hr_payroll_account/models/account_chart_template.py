# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from leewise import models


class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    def _configure_payroll_account_lu(self, companies):
        account_codes = [
        ]
        default_account = False
        rules_mapping = defaultdict(dict)

        # ================================================ #
        #          LUX Employee Payroll Structure          #
        # ================================================ #

        self._configure_payroll_account(
            companies,
            "LU",
            account_codes=account_codes,
            rules_mapping=rules_mapping,
            default_account=default_account)
