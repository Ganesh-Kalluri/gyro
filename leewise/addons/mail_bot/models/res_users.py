# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from markupsafe import Markup

from leewise import models, fields, _

class Users(models.Model):
    _inherit = 'res.users'

    leewisebot_state = fields.Selection(
        [
            ('not_initialized', 'Not initialized'),
            ('onboarding_emoji', 'Onboarding emoji'),
            ('onboarding_attachement', 'Onboarding attachment'),
            ('onboarding_command', 'Onboarding command'),
            ('onboarding_ping', 'Onboarding ping'),
            ('idle', 'Idle'),
            ('disabled', 'Disabled'),
        ], string="LeewiseBot Status", readonly=True, required=False)  # keep track of the state: correspond to the code of the last message sent
    leewisebot_failed = fields.Boolean(readonly=True)

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ['leewisebot_state']

    def _init_messaging(self):
        leewisebot_onboarding = False
        if self.leewisebot_state in [False, 'not_initialized'] and self._is_internal():
            leewisebot_onboarding = True
            self._init_leewisebot()
        res = super()._init_messaging()
        res['leewisebotOnboarding'] = leewisebot_onboarding
        return res

    def _init_leewisebot(self):
        self.ensure_one()
        leewisebot_id = self.env['ir.model.data']._xmlid_to_res_id("base.partner_root")
        channel = self.env['discuss.channel'].channel_get([leewisebot_id, self.partner_id.id])
        message = Markup("%s<br/>%s<br/><b>%s</b> <span class=\"o_leewisebot_command\">:)</span>") % (
            _("Hello,"),
            _("Leewise's chat helps employees collaborate efficiently. I'm here to help you discover its features."),
            _("Try to send me an emoji")
        )
        channel.sudo().message_post(body=message, author_id=leewisebot_id, message_type="comment", subtype_xmlid="mail.mt_comment")
        self.sudo().leewisebot_state = 'onboarding_emoji'
        return channel
