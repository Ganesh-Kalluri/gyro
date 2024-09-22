#  -*- coding: utf-8 -*-
#  Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def _get_fields_stock_barcode(self):
        """ Inject the field 'quality_check_todo' in the initial state of the barcode view.
        """
        fields = super(MrpProduction, self)._get_fields_stock_barcode()
        fields.append('quality_check_todo')
        return fields
