# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from datetime import date

from leewise import api, models, _
from leewise.exceptions import UserError


class ReportHrSalaryEmployeeBymonth(models.AbstractModel):
    _name = 'report.l10n_in_hr_payroll.report_hrsalarybymonth'
    _description = "Indian Salary by Month Report"

    def get_periods(self, form):
        # Get start year-month-date and end year-month-date
        first_year = int(form['start_date'][0:4])
        last_year = int(form['end_date'][0:4])

        first_month = int(form['start_date'][5:7])
        last_month = int(form['end_date'][5:7])
        no_months = (last_year - first_year) * 12 + last_month - first_month + 1
        current_month = first_month
        current_year = first_year

        # Get name of the months from integer
        mnth_name = []
        total_mnths = []
        months = []
        for count in range(0, no_months):
            total_mnths.append(0)
            m = date(current_year, current_month, 1).strftime('%b')
            mnth_name.append(m)
            months.append(str(current_month) + '-' + str(current_year))
            if current_month == 12:
                current_month = 0
                current_year = last_year
            current_month = current_month + 1
        return mnth_name, months, total_mnths

    def get_salary(self, form, emp_id, emp_salary, total_mnths, mnths):
        category_id = form.get('category_id', [])
        category_id = category_id and category_id[0] or False
        self.env.cr.execute("""
                            select to_char(p.date_to,'mm-yyyy') as to_date ,sum(pl.total)
                            from hr_payslip_line as pl
                            left join hr_payslip as p on pl.slip_id = p.id
                            left join hr_employee as emp on emp.id = p.employee_id
                            left join resource_resource as r on r.id = emp.resource_id
                            where p.state = 'done' and p.employee_id = %s and pl.category_id = %s
                            group by r.name, p.date_to,emp.id""",
                            (emp_id, category_id,))
        sal = self.env.cr.fetchall()
        salary = dict(sal)
        total = 0.0
        cnt = 0
        for month in mnths:
            if len(month) != 7:
                month = '0' + str(month)
            if month in salary and salary[month]:
                emp_salary.append(salary[month])
                total += salary[month]
                total_mnths[cnt] = total_mnths[cnt] + salary[month]
            else:
                emp_salary.append(0.00)
            cnt = cnt + 1
        return emp_salary, total, total_mnths

    def get_employee(self, form, mnths, total_mnths):
        emp_salary = []
        salary_list = []
        emp_ids = form.get('employee_ids', [])
        employees = self.env['hr.employee'].browse(emp_ids)

        for emp_id in employees:
            emp_salary.append(emp_id.name)
            total = 0.0
            emp_salary, total, total_mnths = self.get_salary(form, emp_id.id, emp_salary, total_mnths, mnths)
            emp_salary.append(total)
            salary_list.append(emp_salary)
            emp_salary = []
        return salary_list

    def get_months_tol(self):
        return []

    def get_total(self, mnths_total):
        total = 0.0
        for item in mnths_total:
            for count in range(1, len(item)):
                total += item[count]
        return total

    @api.model
    def _get_report_values(self, docids, data=None):
        if not data.get('form') or not self.env.context.get('active_model') or not self.env.context.get('active_id'):
            raise UserError(_("Form content is missing, this report cannot be printed."))

        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))
        get_periods, months, total_mnths = self.get_periods(data['form'])
        get_employee = self.get_employee(data['form'], months, total_mnths)
        get_total = self.get_total([total_mnths])

        return {
            'doc_ids': docids,
            'doc_model': model,
            'data': data,
            'docs': docs,
            'get_periods': get_periods,
            'get_employee': get_employee,
            'get_months_tol': [total_mnths],
            'get_total': get_total,
            'month_len': len(total_mnths) + 1
        }
