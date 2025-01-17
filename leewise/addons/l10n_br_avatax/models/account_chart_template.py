# Part of Leewise. See LICENSE file for full copyright and licensing details.
from leewise import models
from leewise.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('br', 'account.tax')
    def _get_br_avatax_account_tax(self):
        return {
            'tax_template_out_aproxtrib_fed_incl_goods': {'l10n_br_avatax_code': 'aproxtribFed'},
            'tax_template_out_aproxtrib_fed_excl_goods': {'l10n_br_avatax_code': 'aproxtribFed'},
            'tax_template_out_aproxtrib_state_incl_goods': {'l10n_br_avatax_code': 'aproxtribState'},
            'tax_template_out_aproxtrib_state_excl_goods': {'l10n_br_avatax_code': 'aproxtribState'},
            'tax_template_out_cofins_incl_goods': {'l10n_br_avatax_code': 'cofins'},
            'tax_template_out_cofins_excl_goods': {'l10n_br_avatax_code': 'cofins'},
            'tax_template_out_cofins_deson_incl_goods': {'l10n_br_avatax_code': 'cofinsDeson'},
            'tax_template_out_cofins_deson_excl_goods': {'l10n_br_avatax_code': 'cofinsDeson'},
            'tax_template_out_cofins_st_incl_goods': {'l10n_br_avatax_code': 'cofinsSt'},
            'tax_template_out_cofins_st_excl_goods': {'l10n_br_avatax_code': 'cofinsSt'},
            'tax_template_out_icms_incl_goods': {'l10n_br_avatax_code': 'icms'},
            'tax_template_out_icms_excl_goods': {'l10n_br_avatax_code': 'icms'},
            'tax_template_out_icms_credsn_incl_goods': {'l10n_br_avatax_code': 'icmsCredsn'},
            'tax_template_out_icms_credsn_excl_goods': {'l10n_br_avatax_code': 'icmsCredsn'},
            'tax_template_out_icms_deson_incl_goods': {'l10n_br_avatax_code': 'icmsDeson'},
            'tax_template_out_icms_deson_excl_goods': {'l10n_br_avatax_code': 'icmsDeson'},
            'tax_template_out_icms_difa_dest_incl_goods': {'l10n_br_avatax_code': 'icmsDifaDest'},
            'tax_template_out_icms_difa_dest_excl_goods': {'l10n_br_avatax_code': 'icmsDifaDest'},
            'tax_template_out_icms_difa_fcp_incl_goods': {'l10n_br_avatax_code': 'icmsDifaFCP'},
            'tax_template_out_icms_difa_fcp_excl_goods': {'l10n_br_avatax_code': 'icmsDifaFCP'},
            'tax_template_out_icms_difa_remet_incl_goods': {'l10n_br_avatax_code': 'icmsDifaRemet'},
            'tax_template_out_icms_difa_remet_excl_goods': {'l10n_br_avatax_code': 'icmsDifaRemet'},
            'tax_template_out_icms_eff_incl_goods': {'l10n_br_avatax_code': 'icmsEff'},
            'tax_template_out_icms_eff_excl_goods': {'l10n_br_avatax_code': 'icmsEff'},
            'tax_template_out_icms_fcp_incl_goods': {'l10n_br_avatax_code': 'icmsFCP'},
            'tax_template_out_icms_fcp_excl_goods': {'l10n_br_avatax_code': 'icmsFCP'},
            'tax_template_out_icms_own_payer_incl_goods': {'l10n_br_avatax_code': 'icmsOwnPayer'},
            'tax_template_out_icms_own_payer_excl_goods': {'l10n_br_avatax_code': 'icmsOwnPayer'},
            'tax_template_out_icms_part_incl_goods': {'l10n_br_avatax_code': 'icmsPart'},
            'tax_template_out_icms_part_excl_goods': {'l10n_br_avatax_code': 'icmsPart'},
            'tax_template_out_icms_rf_incl_goods': {'l10n_br_avatax_code': 'icmsRf'},
            'tax_template_out_icms_rf_excl_goods': {'l10n_br_avatax_code': 'icmsRf'},
            'tax_template_out_icms_st_incl_goods': {'l10n_br_avatax_code': 'icmsSt'},
            'tax_template_out_icms_st_excl_goods': {'l10n_br_avatax_code': 'icmsSt'},
            'tax_template_out_icms_st_fcp_incl_goods': {'l10n_br_avatax_code': 'icmsStFCP'},
            'tax_template_out_icms_st_fcp_excl_goods': {'l10n_br_avatax_code': 'icmsStFCP'},
            'tax_template_out_icms_st_fcppart_incl_goods': {'l10n_br_avatax_code': 'icmsStFCPPart'},
            'tax_template_out_icms_st_fcppart_excl_goods': {'l10n_br_avatax_code': 'icmsStFCPPart'},
            'tax_template_out_icms_st_part_incl_goods': {'l10n_br_avatax_code': 'icmsStPart'},
            'tax_template_out_icms_st_part_excl_goods': {'l10n_br_avatax_code': 'icmsStPart'},
            'tax_template_out_icms_st_sd_incl_goods': {'l10n_br_avatax_code': 'icmsStSd'},
            'tax_template_out_icms_st_sd_excl_goods': {'l10n_br_avatax_code': 'icmsStSd'},
            'tax_template_out_icms_st_sd_fcp_incl_goods': {'l10n_br_avatax_code': 'icmsStSdFCP'},
            'tax_template_out_icms_st_sd_fcp_excl_goods': {'l10n_br_avatax_code': 'icmsStSdFCP'},
            'tax_template_out_ii_incl_goods': {'l10n_br_avatax_code': 'ii'},
            'tax_template_out_ii_excl_goods': {'l10n_br_avatax_code': 'ii'},
            'tax_template_out_iof_incl_goods': {'l10n_br_avatax_code': 'iof'},
            'tax_template_out_iof_excl_goods': {'l10n_br_avatax_code': 'iof'},
            'tax_template_out_ipi_incl_goods': {'l10n_br_avatax_code': 'ipi'},
            'tax_template_out_ipi_excl_goods': {'l10n_br_avatax_code': 'ipi'},
            'tax_template_out_ipi_returned_incl_goods': {'l10n_br_avatax_code': 'ipiReturned'},
            'tax_template_out_ipi_returned_excl_goods': {'l10n_br_avatax_code': 'ipiReturned'},
            'tax_template_out_pis_incl_goods': {'l10n_br_avatax_code': 'pis'},
            'tax_template_out_pis_excl_goods': {'l10n_br_avatax_code': 'pis'},
            'tax_template_out_pis_deson_incl_goods': {'l10n_br_avatax_code': 'pisDeson'},
            'tax_template_out_pis_deson_excl_goods': {'l10n_br_avatax_code': 'pisDeson'},
            'tax_template_out_pis_st_incl_goods': {'l10n_br_avatax_code': 'pisSt'},
            'tax_template_out_pis_st_excl_goods': {'l10n_br_avatax_code': 'pisSt'},
        }

    @template('br', 'account.fiscal.position')
    def _get_br_avatax_fiscal_position(self):
        return {
            'account_fiscal_position_avatax_br': {
                'name': 'Automatic Tax Mapping (Avalara Brazil)',
                'l10n_br_is_avatax': True,
                'country_id': self.env.ref('base.br').id,
            }
        }
