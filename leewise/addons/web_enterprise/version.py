# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

import leewise

# ----------------------------------------------------------
# Monkey patch release to set the edition as 'enterprise'
# ----------------------------------------------------------
leewise.release.version_info = leewise.release.version_info[:5] + ('e',)
if '+e' not in leewise.release.version:     # not already patched by packaging
    leewise.release.version = '{0}+e{1}{2}'.format(*leewise.release.version.partition('-'))

leewise.service.common.RPC_VERSION_1.update(
    server_version=leewise.release.version,
    server_version_info=leewise.release.version_info)
