# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

{
    'name': 'French Payroll',
    'countries': ['fr'],
    'category': 'Human Resources/Payroll',
    'author': 'Yannick Buron (SYNERPGY)',
    'depends': ['hr_payroll', 'l10n_fr'],
    'description': """
French Payroll Rules.
=====================

    - Configuration of hr_payroll for French localization
    - All main contributions rules for French payslip, for 'cadre' and 'non-cadre'
    - New payslip report

TODO:
-----
    - Integration with holidays module for deduction and allowance
    - Integration with hr_payroll_account for the automatic account_move_line
      creation from the payslip
    - Continue to integrate the contribution. Only the main contribution are
      currently implemented
    - Remake the report under webkit
    - The payslip.line with appears_in_payslip = False should appears in the
      payslip interface, but not in the payslip report
    """,
    'data': [
        'data/l10n_fr_hr_payroll_data.xml',
        'data/l10n_fr_hr_payroll_employe_cadre_data.xml',
        'data/l10n_fr_hr_payroll_employe_non_cadre_data.xml',
        'views/l10n_fr_hr_payroll_view.xml',
        'views/res_config_settings_views.xml',
        'report/report_l10n_fr_fiche_paye.xml',
        'report/l10n_fr_hr_payroll_report.xml',
    ],
    'license': 'OEEL-1',
}
