# Part of Leewise. See LICENSE file for full copyright and licensing details.

{
    "name": "VoIP",
    "summary": """Make and receive phone calls from within Leewise.""",
    "description": """Adds a softphone and helpers to make phone calls directly from within your Leewise database.""",
    "category": "Productivity/VOIP",
    "sequence": 280,
    "version": "2.0",
    "depends": ["base", "mail", "phone_validation", "web", "web_mobile"],
    "data": [
        "security/ir.model.access.csv",
        "security/voip_security.xml",
        "views/res_config_settings_views.xml",
        "views/res_partner_views.xml",
        "views/res_users_views.xml",
        "views/res_users_settings_views.xml",
        "views/voip_call_views.xml",
    ],
    "application": True,
    "license": "OEEL-1",
    "assets": {
        "voip.assets_sip": [
            "voip/static/lib/sip.js"
        ],
        "web.assets_backend": [
            "voip/static/src/**/*",
            ("remove", "voip/static/src/**/*.dark.scss"),
        ],
        "web.assets_web_dark": [
            "voip/static/src/**/*.dark.scss",
        ],
        "web.tests_assets": [
            "voip/static/tests/helpers/**/*.js",
        ],
        "web.qunit_suite_tests": [
            "voip/static/tests/**/*.js",
            ("remove", "voip/static/tests/helpers/**/*"),
            ("remove", "voip/static/tests/**/*.mobile.js"),
        ],
        "web.qunit_mobile_suite_tests": [
            "voip/static/tests/**/*.mobile.js",
        ],
    },
}
