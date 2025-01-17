# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import _, api, models

from leewise.exceptions import UserError


class UtmCampaign(models.Model):
    _inherit = 'utm.campaign'

    @api.ondelete(at_uninstall=False)
    def _unlink_except_linked_marketing_campaigns(self):
        """ Already handled by ondelete='restrict', but let's show a nice error message """
        linked_marketing_campaigns = self.env['marketing.campaign'].sudo().search([
            ('utm_campaign_id', 'in', self.ids)
        ])

        if linked_marketing_campaigns:
            raise UserError(_(
                "You cannot delete these UTM Campaigns as they are linked to the following marketing campaigns in "
                "Marketing Automation:\n%(campaign_names)s",
                campaign_names=', '.join(['"%s"' % name for name in linked_marketing_campaigns.mapped('name')])))
