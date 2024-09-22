# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import api, models, fields, _
from leewise.exceptions import UserError


class l10nChSocialInsurance(models.Model):
    _name = 'l10n.ch.social.insurance'
    _description = 'Swiss: Social Insurances (AVS, AC)'

    name = fields.Char(required=True)
    member_number = fields.Char()
    member_subnumber = fields.Char()
    # https://www.swissdec.ch/fileadmin/user_upload/_Datenempfaenger/Empfaengerliste.pdf
    insurance_company = fields.Selection([
        ('048.000', 'AK Aargauer Arbeitgeber'),
        ('103.000', 'AK agrapi'),
        ('074.000', 'AK ALBICOLAC'),
        ('015.000', 'AK Appenzell A.Rh.'),
        ('016.000', 'AK Appenzell I.Rh.'),
        ('040.000', 'AK Arbeitgeber Basel'),
        ('089.000', 'AK Banken'),
        ('012.000', 'AK Basel Stadt'),
        ('066.000', 'AK Baumeister'),
        ('002.000', 'AK Bern'),
        ('087.000', 'AK Bündner Gewerbe'),
        ('106.007', 'AK Caisse de compensation FER VALAIS SION'),
        ('035.000', 'AK scienceindustries'),
        ('113.000', 'AK Coiffure und Esthétique'),
        ('031.000', 'AK Coop'),
        ('114.000', 'AK der Wirtschaftskammer Baselland'),
        ('026.001', 'AK Eidg. Ausgleichskasse'),
        ('037.000', 'AK Elektrizitätswerke'),
        ('095.000', 'AK EXFOUR'),
        ('106.005', 'AK FER CIAB'),
        ('106.001', 'AK FER CIAM'),
        ('106.004', 'AK FER CIAN'),
        ('106.002', 'AK FER CIFA'),
        ('106.003', 'AK FER CIGA'),
        ('098.000', 'AK Forte'),
        ('046.000', 'AK GastroSocial'),
        ('107.000', 'AK Geschäftsinhaber Bern'),
        ('112.000', 'AK Gewerbe St. Gallen'),
        ('101.000', 'AK Holz'),
        ('003.000', 'AK Luzern'),
        ('028.000', 'AK Medisuisse'),
        ('034.000', 'AK Metzger'),
        ('070.000', 'AK Migros'),
        ('078.000', 'AK Milch'),
        ('033.000', 'AK MOBIL'),
        ('007.000', 'AK Nidwalden'),
        ('006.000', 'AK Obwalden'),
        ('032.000', 'AK Ostschweizerischer Handel'),
        ('038.000', 'AK Panvica'),
        ('115.000', 'AK Privatkliniken'),
        ('099.000', 'AK PROMEA'),
        ('105.000', 'AK Schweiz. Gewerbe'),
        ('005.000', 'AK Schwyz'),
        ('030.000', 'AK Simulac'),
        ('011.000', 'AK Solothurn'),
        ('079.000', 'AK Spida'),
        ('045.000', 'AK Spirituosen'),
        ('013.000', 'AK SVA Basel Land'),
        ('017.000', 'AK SVA St. Gallen'),
        ('060.000', 'AK Swissmem'),
        ('117.000', 'AK Swisstempcomp'),
        ('020.000', 'AK Thurgau'),
        ('055.000', 'AK Thurgauer Gewerbe'),
        ('069.000', 'AK Transport'),
        ('051.000', 'AK Uhrenindustrie CCIH - Zentralverwaltung'),
        ('051.003', 'AK Uhrenindustrie CCIH - Agence 51.3'),
        ('051.004', 'AK Uhrenindustrie CCIH - Agentur 51.4'),
        ('051.005', 'AK Uhrenindustrie CCIH - Agentur 51.5'),
        ('051.007', 'AK Uhrenindustrie CCIH - Agentur 51.7'),
        ('051.010', 'AK Uhrenindustrie CCIH - Agentur 10'),
        ('004.000', 'AK Uri'),
        ('023.000', 'AK Wallis / CC Valais'),
        ('022.000', 'AK Vaud'),
        ('081.000', 'AK Versicherung x x x swissdec@insite.ch'),
        ('009.000', 'AK Zug'),
        ('065.000', 'AK Zürcher Arbeitgeber'),
        ('110.000', 'Caisse AVS de la Fédération patronale vaudoise'),
        ('010.000', 'Caisse AVS Fribourg'),
        ('150.000', 'Caisse de compensation du canton du Jura'),
        ('021.000', 'Cassa cantonale di compensazione AVS'),
        ('024.000', 'Caisse cantonale neuchâteloise de compensation (CCNC)'),
        ('109.000', "Chambre vaudoise du commerce et de l'industrie (CVCI)"),
        ('066.002', 'CCB Genève'),
        ('059.000', 'CICICAM / CINALFA'),
        ('071.000', 'Handel Schweiz'),
        ('044.000', 'Hotela Caisse de Compensation'),
        ('025.000', 'OCAS Genève, caisse genevoise de compensation (CCGC)'),
        ('008.000', 'Sozialversicherungen Glarus'),
        ('019.000', 'SVA Aargau'),
        ('018.000', 'SVA Graubünden'),
        ('014.000', 'SVA Schaffhausen'),
        ('001.000', 'SVA Zürich'),
    ])
    insurance_code = fields.Char(compute="_compute_insurance_code")
    avs_line_ids = fields.One2many('l10n.ch.social.insurance.avs.line', 'insurance_id')
    ac_line_ids = fields.One2many('l10n.ch.social.insurance.ac.line', 'insurance_id')

    @api.depends('insurance_company')
    def _compute_insurance_code(self):
        for insurance in self:
            insurance.insurance_code = insurance.insurance_company

    def _get_avs_rates(self, target):
        if not self:
            return 0, 0
        for line in self.avs_line_ids:
            if line.date_from <= target and (not line.date_to or target <= line.date_to):
                return line.employee_rate, line.employer_rate
        raise UserError(_('No AVS rates found for date %s', target))

    def _get_ac_rates(self, target):
        if not self:
            return 0, 0
        for line in self.ac_line_ids:
            if line.date_from <= target and (not line.date_to or target <= line.date_to):
                return line.employee_rate, line.employer_rate
        raise UserError(_('No AC rates found for date %s', target))

    def _get_additional_ac_rates(self, target):
        if not self:
            return 0, 0
        for line in self.ac_line_ids:
            if line.date_from <= target and (not line.date_to or target <= line.date_to):
                return line.employee_additional_rate, line.employer_additional_rate
        raise UserError(_('No AC rates found for date %s', target))


class l10nChSocialInsuranceAVSLine(models.Model):
    _name = 'l10n.ch.social.insurance.avs.line'
    _description = 'Swiss: Social Insurances - AVS Line'

    date_from = fields.Date(string="From", required=True)
    date_to = fields.Date(string="To")
    insurance_id = fields.Many2one('l10n.ch.social.insurance')
    employee_rate = fields.Float(string="Employee Rate (%)", default=5.3)
    employer_rate = fields.Float(string="Company Rate (%)", default=5.3)


class l10nChSocialInsuranceACLine(models.Model):
    _name = 'l10n.ch.social.insurance.ac.line'
    _description = 'Swiss: Social Insurances - AC Line'

    date_from = fields.Date(string="From", required=True)
    date_to = fields.Date(string="To")
    insurance_id = fields.Many2one('l10n.ch.social.insurance')
    employee_rate = fields.Float(string="Employee Rate (%)", digits='Payroll Rate', default=1.1)
    employer_rate = fields.Float(string="Company Rate (%)", digits='Payroll Rate', default=1.1)
    employee_additional_rate = fields.Float(string="Employee Additional Rate (%)", digits='Payroll Rate', default=0.5)
    employer_additional_rate = fields.Float(string="Company Additional Rate (%)", digits='Payroll Rate', default=0)