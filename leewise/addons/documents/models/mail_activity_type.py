# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, fields


class MailActivityType(models.Model):
    _inherit = "mail.activity.type"

    tag_ids = fields.Many2many('documents.tag')
    folder_id = fields.Many2one('documents.folder',
                                help="By defining a folder, the upload activities will generate a document")
