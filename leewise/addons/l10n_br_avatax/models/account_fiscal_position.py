# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import models, fields


class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    l10n_br_is_avatax = fields.Boolean('Use Avatax Brazil API')
