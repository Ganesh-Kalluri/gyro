# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models

class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _get_mail_thread_data(self, request_list):
        res = super()._get_mail_thread_data(request_list)
        res['canSendWhatsapp'] = self.env['whatsapp.template']._can_use_whatsapp(self._name)
        return res
