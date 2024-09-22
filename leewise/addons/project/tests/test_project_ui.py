# Part of Leewise. See LICENSE file for full copyright and licensing details.

import leewise.tests


@leewise.tests.tagged('post_install', '-at_install')
class TestUi(leewise.tests.HttpCase):

    def test_01_project_tour(self):
        self.start_tour("/web", 'project_tour', login="admin")
