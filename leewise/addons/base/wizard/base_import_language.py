# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

import base64
import logging
import operator
from tempfile import TemporaryFile
from os.path import splitext

from leewise import api, fields, models, tools, sql_db, _
from leewise.exceptions import UserError
from leewise.tools.translate import TranslationImporter

_logger = logging.getLogger(__name__)


class BaseLanguageImport(models.TransientModel):
    _name = "base.language.import"
    _description = "Language Import"

    name = fields.Char('Language Name', required=True)
    code = fields.Char('ISO Code', size=6, required=True,
                       help="ISO Language and Country code, e.g. en_US")
    data = fields.Binary('File', required=True, attachment=False)
    filename = fields.Char('File Name', required=True)
    overwrite = fields.Boolean('Overwrite Existing Terms',
                               default=True,
                               help="If you enable this option, existing translations (including custom ones) "
                                    "will be overwritten and replaced by those in this file")

    def import_lang(self):
        Lang = self.env["res.lang"]
        for overwrite, base_lang_imports in tools.groupby(self, operator.itemgetter('overwrite')):
            translation_importer = TranslationImporter(self.env.cr)
            for base_lang_import in base_lang_imports:
                if not Lang._activate_lang(base_lang_import.code):
                    Lang._create_lang(base_lang_import.code, lang_name=base_lang_import.name)
                try:
                    with TemporaryFile('wb+') as buf:
                        buf.write(base64.decodebytes(base_lang_import.data))
                        fileformat = splitext(base_lang_import.filename)[-1][1:].lower()
                        translation_importer.load(buf, fileformat, base_lang_import.code)
                except Exception as e:
                    _logger.warning('Could not import the file due to a format mismatch or it being malformed.')
                    raise UserError(
                        _('File %r not imported due to format mismatch or a malformed file.'
                          ' (Valid formats are .csv, .po)\n\nTechnical Details:\n%s',
                          base_lang_import.filename, tools.ustr(e))
                    )
            translation_importer.save(overwrite=overwrite)
        return True