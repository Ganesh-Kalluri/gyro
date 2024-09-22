# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.http import request, route
from leewise.addons.mail.controllers.webclient import WebclientController
from leewise.addons.mail.models.discuss.mail_guest import add_guest_to_context


class WebClient(WebclientController):
    @route("/web/tests/livechat", type="http", auth="user")
    def test_external_livechat(self, **kwargs):
        return request.render("im_livechat.qunit_embed_suite", {
            "server_url": request.env["ir.config_parameter"].get_base_url(),
        })
