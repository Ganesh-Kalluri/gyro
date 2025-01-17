# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

{
    'name': 'LeewiseBot',
    'version': '1.2',
    'category': 'Productivity/Discuss',
    'summary': 'Add LeewiseBot in discussions',
    'website': 'https://www.leewise.in/app/discuss',
    'depends': ['mail'],
    'auto_install': True,
    'installable': True,
    'data': [
        'views/res_users_views.xml',
        'data/mailbot_data.xml',
    ],
    'demo': [
        'data/mailbot_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mail_bot/static/src/scss/leewisebot_style.scss',
        ],
    },
    'license': 'LGPL-3',
}
