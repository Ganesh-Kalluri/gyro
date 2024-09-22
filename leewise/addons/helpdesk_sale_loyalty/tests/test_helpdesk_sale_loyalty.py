# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.addons.helpdesk.tests import common
from leewise.tests.common import Form


class TestHelpdeskSaleCoupon(common.HelpdeskCommon):
    """ Test used to check that the functionalities of After sale in Helpdesk (sale_coupon).
    """

    def test_helpdesk_sale_loyalty(self):
        # give the test team ability to create coupons
        self.test_team.use_coupons = True

        ticket = self.env['helpdesk.ticket'].create({
            'name': 'test',
            'partner_id': self.partner.id,
            'team_id': self.test_team.id,
        })
        program = self.env['loyalty.program'].create({
            'name': 'test program',
            'program_type': 'coupons',
            'trigger': 'with_code',
            'applies_on': 'current',
            'reward_ids': [(0, 0, {
                'reward_type': 'discount',
                'discount': 10,
                'discount_mode': 'percent',
                'discount_applicability': 'order',
            })],
        })

        coupon_form = Form(self.env['helpdesk.sale.coupon.generate'].with_context({
            'active_model': 'helpdesk.ticket',
            'default_ticket_id': ticket.id,
        }))
        coupon_form.program = program
        sale_coupon = coupon_form.save()
        sale_coupon.action_coupon_generate_send()

        coupon = self.env['loyalty.card'].search([
            ('partner_id', '=', self.partner.id),
            ('program_id', '=', program.id)
        ])

        self.assertEqual(len(coupon), 1, "No coupon created")
        self.assertEqual(len(ticket.coupon_ids), 1,
            "The ticket is not linked to a coupon")
        self.assertEqual(coupon[0], ticket.coupon_ids[0],
            "The correct coupon should be referenced in the ticket")