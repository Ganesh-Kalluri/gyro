# coding: utf-8
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import models, fields


class AvataxValidateAddress(models.TransientModel):
    _inherit = 'avatax.validate.address'

    def action_save_validated(self):
        res = super().action_save_validated()
        for wizard in self:
            wizard.partner_id.write({
                'date_localization': fields.Date.context_today(wizard.partner_id),
                'is_avatax_valid': True,
            })
        return res
