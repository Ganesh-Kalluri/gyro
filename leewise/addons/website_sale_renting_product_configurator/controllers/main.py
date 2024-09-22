# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import fields, http

from leewise.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleRenting(WebsiteSale):

    @http.route()
    def cart_options_update_json(self, *args, start_date=None, end_date=None, **kwargs):
        start_date = fields.Datetime.to_datetime(start_date)
        end_date = fields.Datetime.to_datetime(end_date)
        return super().cart_options_update_json(
            *args, start_date=start_date, end_date=end_date, **kwargs
        )
