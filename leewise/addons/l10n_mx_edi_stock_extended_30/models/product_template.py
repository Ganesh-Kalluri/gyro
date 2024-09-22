# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    l10n_mx_edi_material_type = fields.Selection(
        selection=[
            ('01', 'Materia prima'),
            ('02', 'Materia procesada'),
            ('03', 'Materia terminada(producto terminado)'),
            ('04', 'Materia para la industria manufacturera'),
            ('05', 'Otra'),
        ],
        string="Material Type",
        help="State of the material or product when performing a foreign trade operation.",
    )
    l10n_mx_edi_material_description = fields.Char(
        string="Material Description",
        help="Description of the state of the material or product when performing a foreign trade operation.",
    )
