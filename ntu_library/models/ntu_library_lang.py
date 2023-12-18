from odoo import fields, models


class NTULibraryLang(models.Model):
    _name = 'ntu.library.lang'
    _description = 'NTU Library Language'

    name = fields.Char(string='Language', size=100, required=True)
