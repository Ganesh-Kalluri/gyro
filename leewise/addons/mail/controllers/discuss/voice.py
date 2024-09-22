# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import http
from leewise.http import request
from leewise.tools import file_open


class VoiceController(http.Controller):

    @http.route("/discuss/voice/worklet_processor", methods=["GET"], type="http", auth="public")
    def voice_worklet_processor(self):
        return request.make_response(
            file_open("mail/static/src/discuss/voice_message/worklets/processor.js", "rb").read(),
            headers=[
                ("Content-Type", "application/javascript"),
            ],
        )
