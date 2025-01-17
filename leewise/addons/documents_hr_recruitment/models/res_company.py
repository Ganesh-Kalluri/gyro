# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models, api, _


class ResCompany(models.Model):
    _inherit = "res.company"

    documents_recruitment_settings = fields.Boolean(default=False)
    recruitment_folder_id = fields.Many2one('documents.folder', string="Recruitment Workspace", check_company=True,
                                            default=lambda self: self.env.ref('documents_hr_recruitment.documents_recruitment_folder',
                                                                              raise_if_not_found=False))
    recruitment_tag_ids = fields.Many2many('documents.tag', 'recruitment_tags_rel')
