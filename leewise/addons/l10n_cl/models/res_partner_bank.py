# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import fields, models


class ResBank(models.Model):
    _name = 'res.bank'
    _inherit = 'res.bank'

    l10n_cl_sbif_code = fields.Char('Cod. SBIF', size=10)
