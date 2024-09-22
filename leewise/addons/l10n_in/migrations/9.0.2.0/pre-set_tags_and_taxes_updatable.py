# -*- coding: utf-8 -*-

import leewise

def migrate(cr, version):
    registry = leewise.registry(cr.dbname)
    from leewise.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_in')
