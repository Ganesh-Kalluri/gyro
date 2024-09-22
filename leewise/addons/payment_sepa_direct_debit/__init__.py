# Part of Leewise. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models

from leewise.addons.payment import reset_payment_provider


def uninstall_hook(env):
    reset_payment_provider(env, 'sepa_direct_debit')
