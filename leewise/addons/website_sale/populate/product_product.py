# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models
from leewise.tools import populate


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def _populate_get_product_factories(self):
        """Populate the invoice_policy of product.product & product.template models."""
        return super()._populate_get_product_factories() + [
            ('is_published', populate.randomize([True, False], [8, 2]))]