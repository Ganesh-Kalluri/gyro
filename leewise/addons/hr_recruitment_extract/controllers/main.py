# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import http
from leewise.http import request


class HrRecruitmentExtractController(http.Controller):
    @http.route('/hr_recruitment_extract/request_done/<string:extract_document_uuid>', type='http', auth='public', csrf=False)
    def request_done(self, extract_document_uuid):
        """ This webhook is called when the extraction server is done processing a request."""
        applicant_to_update = request.env['hr.applicant'].sudo().search([
            ('extract_document_uuid', '=', extract_document_uuid),
            ('extract_state', 'in', ['waiting_extraction', 'extract_not_ready']),
            ('is_in_extractable_state', '=', True)])
        for applicant in applicant_to_update:
            applicant._check_ocr_status()
        return 'OK'
