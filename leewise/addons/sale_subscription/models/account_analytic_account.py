# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    subscription_ids = fields.One2many('sale.order', 'analytic_account_id', string='Subscriptions')
    subscription_count = fields.Integer(compute='_compute_subscription_count', string='Subscription Count')

    def _compute_subscription_count(self):
        subscription_data = self.env['sale.order']._read_group(domain=[('analytic_account_id', 'in', self.ids)],
                                                                     groupby=['analytic_account_id'],
                                                                     aggregates=['__count'])
        mapped_data = {analytic_account.id: count for analytic_account, count in subscription_data}
        for account in self:
            account.subscription_count = mapped_data.get(account.id, 0)

    def subscriptions_action(self):
        subscription_ids = self.mapped('subscription_ids').ids
        result = {
            "type": "ir.actions.act_window",
            "res_model": "sale.order",
            "views": [[False, "tree"], [False, "form"]],
            "domain": [["id", "in", subscription_ids]],
            "context": {"create": False},
            "name": "Subscriptions",
        }
        if len(subscription_ids) == 1:
            result['views'] = [(False, "form")]
            result['res_id'] = subscription_ids[0]
        return result
