# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_es_tbai_tax_agency = fields.Selection(related='company_id.l10n_es_tbai_tax_agency', readonly=False)
