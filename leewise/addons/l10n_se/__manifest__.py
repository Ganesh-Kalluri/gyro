# Part of Leewise. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sweden - Accounting',
    'website': 'https://www.leewise.in/documentation/17.0/applications/finance/fiscal_localizations.html',
    'icon': '/account/static/description/l10n.png',
    'countries': ['se'],
    'version': '1.0',
    'author': 'XCLUDE, Leewise',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
Swedish Accounting
------------------

This is the base module to manage the accounting chart for Sweden in Leewise.
It also includes the invoice OCR payment reference handling.
    """,
    'depends': [
        'account',
        'base_vat',
    ],
    'data': [
        'data/account.account.tag.csv',
        'data/account_tax_report_data.xml',
        "data/res_country_data.xml",
        'views/partner_view.xml',
        'views/account_journal_view.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
