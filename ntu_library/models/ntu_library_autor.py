from odoo import fields, models


class NTULibraryAutor(models.Model):
    _name = 'ntu.library.autor'
    _description = 'NTU Library Autor'

    name = fields.Char(string='Name', size=150, required=True)
    description = fields.Text()
