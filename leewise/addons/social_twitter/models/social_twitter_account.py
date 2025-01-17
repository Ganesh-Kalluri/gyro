# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, fields


class SocialTwitterAccount(models.Model):
    _name = 'social.twitter.account'
    _description = 'Social Twitter Account'

    name = fields.Char('Name')
    description = fields.Char('Description')
    twitter_id = fields.Char('Twitter ID')
    image = fields.Binary('Image')

    twitter_searched_by_id = fields.Many2one('social.account', 'Searched by')
