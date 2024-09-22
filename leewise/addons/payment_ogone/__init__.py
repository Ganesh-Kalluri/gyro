# Part of Leewise. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models

from leewise.exceptions import UserError
from leewise.tools import config

from leewise.addons.payment import setup_provider, reset_payment_provider


def pre_init_hook(env):
    if not any(config.get(key) for key in ('init', 'update')):
        raise UserError(
            "This module is deprecated and cannot be installed. "
            "Consider installing the Payment Provider: Stripe module instead.")


def post_init_hook(env):
    setup_provider(env, 'ogone')


def uninstall_hook(env):
    reset_payment_provider(env, 'ogone')
