# Part of Leewise. See LICENSE file for full copyright and licensing details.
{
    'name': 'CodaBox',
    'version': '1.0',
    'author': 'Leewise',
    'website': 'https://www.leewise.in/documentation/17.0/applications/finance/fiscal_localizations/belgium.html#codabox',
    'category': 'Accounting/Localizations',
    'summary': 'For Accounting Firms',
    'description': '''This module allows Accounting Firms to connect to CodaBox
and automatically import CODA and SODA statements for their clients in Leewise.
The connection must be done by the Accounting Firm.
    ''',
    'depends': [
        'l10n_be_coda',
        'l10n_be_soda',
    ],
    'auto_install': True,
    'data': [
        'views/res_config_settings_views.xml',
        'views/account_journal_views.xml',
        'data/ir_cron.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'l10n_be_codabox/static/src/components/**/*',
        ],
    },
    'license': 'OEEL-1',
}
