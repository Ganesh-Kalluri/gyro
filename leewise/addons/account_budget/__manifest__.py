# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

{
    'name': 'Budget Management',
    'category': 'Accounting/Accounting',
    'description': """
Use budgets to compare actual with expected revenues and costs
--------------------------------------------------------------
""",
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'security/account_budget_security.xml',
        'views/account_budget_views.xml',
        'views/account_analytic_account_views.xml',
    ],
    'demo': ['data/account_budget_demo.xml'],
    'license': 'OEEL-1',
}
