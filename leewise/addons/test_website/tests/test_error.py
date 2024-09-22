import leewise.tests
from leewise.tools import mute_logger


@leewise.tests.common.tagged('post_install', '-at_install')
class TestWebsiteError(leewise.tests.HttpCase):

    @mute_logger('leewise.addons.http_routing.models.ir_http', 'leewise.http')
    def test_01_run_test(self):
        self.start_tour("/test_error_view", 'test_error_website')
