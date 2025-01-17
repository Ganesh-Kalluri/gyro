# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import _, api, fields, models
from leewise.exceptions import AccessError
from leewise.tools import is_html_empty


class SaleOrderCloseReason(models.Model):
    _name = "sale.order.close.reason"
    _order = "sequence, id"
    _description = "Subscription Close Reason"

    name = fields.Char('Reason', required=True, translate=True)
    sequence = fields.Integer(default=10)

    visible_in_portal = fields.Boolean(default=True, required=True)
    retention_message = fields.Html('Message', translate=True, help="Try to prevent customers from leaving and closing their subscriptions, thanks to a catchy message and a call to action.")
    retention_button_text = fields.Char('Button Text', translate=True)
    retention_button_link = fields.Char('Button Link', translate=True)
    empty_retention_message = fields.Boolean(compute='_compute_empty_retention_message')
    # protected reasons can't be deleted as they are used by leewise bot
    is_protected = fields.Boolean(default=False)

    @api.depends('retention_message')
    def _compute_empty_retention_message(self):
        for reason in self:
            reason.empty_retention_message = is_html_empty(reason.retention_message)

    def write(self, vals):
        vals.pop('is_protected', None)
        return super().write(vals)

    @api.ondelete(at_uninstall=False)
    def _unlink_close_reasons(self):
        for reason in self:
            if reason.is_protected:
                raise AccessError(_("The reason %s is required by the Subscription application and cannot be deleted.", reason.name))
