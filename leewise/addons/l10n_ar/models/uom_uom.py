# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import fields, models


class Uom(models.Model):

    _inherit = 'uom.uom'

    l10n_ar_afip_code = fields.Char('Code', help='Argentina: This code will be used on electronic invoice.')