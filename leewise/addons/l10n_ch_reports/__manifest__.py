# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

{
    'name': 'Switzerland - Accounting Reports',
    'countries': ['ch'],
    'version': '1.1',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting reports for Switzerland
    """,
    'depends': [
        'l10n_ch', 'account_reports'
    ],
    'data': [
        'data/account_financial_html_report_data.xml',
    ],
    'installable': True,
    'auto_install': ['l10n_ch', 'account_reports'],
    'website': 'https://www.leewise.in/app/accounting',
    'license': 'OEEL-1',
}
