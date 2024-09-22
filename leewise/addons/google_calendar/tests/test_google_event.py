# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise.tests.common import BaseCase
from leewise.addons.google_calendar.utils.google_calendar import GoogleEvent


class TestGoogleEvent(BaseCase):
    def test_google_event_readonly(self):
        event = GoogleEvent()
        with self.assertRaises(TypeError):
            event._events['foo'] = 'bar'
        with self.assertRaises(AttributeError):
            event._events.update({'foo': 'bar'})
        with self.assertRaises(TypeError):
            dict.update(event._events, {'foo': 'bar'})
