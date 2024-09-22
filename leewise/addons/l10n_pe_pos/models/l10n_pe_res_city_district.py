# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import fields, models


class L10nPeResCityDistrict(models.Model):
    _inherit = "l10n_pe.res.city.district"

    country_id = fields.Many2one(related="city_id.country_id")
    state_id = fields.Many2one(related="city_id.state_id")
