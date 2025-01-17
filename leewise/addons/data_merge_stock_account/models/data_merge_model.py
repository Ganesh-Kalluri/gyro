# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, models, _


class DataMergeModel(models.Model):
    _inherit = 'data_merge.model'

    @api.onchange('res_model_id')
    def _onchange_res_model_id(self):
        super()._onchange_res_model_id()

        if self.res_model_id.model in ('product.product', 'product.template'):
            return {'warning': {
                'title': _("Warning"),
                'message': _("Merging some products is an important change that will impact your inventory valuation. "
                             "You may have to manually rectify it once done."),
            }}
