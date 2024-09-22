from leewise import models


class ThemeLeewiseExperts(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_leewise_experts_post_copy(self, mod):
        self.enable_view('website.template_header_sales_three')
        self.enable_view('website.template_footer_contact')
