import leewise.tests
from leewise.tools import mute_logger


@leewise.tests.common.tagged('post_install', '-at_install')
class TestWebsiteSession(leewise.tests.HttpCase):

    def test_01_run_test(self):
        self.start_tour('/', 'test_json_auth')
