# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.http import request, route

from leewise.addons.website_sale.controllers.variant import WebsiteSaleVariantController


class WebsiteSaleStockVariantController(WebsiteSaleVariantController):

    @route()
    def get_combination_info_website(self, *args, **kwargs):
        request.update_context(website_sale_stock_get_quantity=True)
        return super().get_combination_info_website(*args, **kwargs)
