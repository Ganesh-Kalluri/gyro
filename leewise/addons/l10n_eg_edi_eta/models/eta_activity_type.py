# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.


from leewise import models, fields, api
from leewise.osv import expression


class EtaActivityType(models.Model):
    _name = 'l10n_eg_edi.activity.type'
    _description = 'ETA code for activity type'

    name = fields.Char(required=True, translate=True)
    code = fields.Char(required=True)

    @api.model
    def _name_search(self, name, domain=None, operator='ilike', limit=None, order=None):
        domain = domain or []
        if operator != 'ilike' or not (name or '').strip():
            # ignore 'ilike' with name containing only spaces
            domain = expression.AND([['|', ('name', operator, name), ('code', operator, name)], domain])
        return self._search(domain, limit=limit, order=order)
