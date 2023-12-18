from odoo import fields, models


class GenresLiterature(models.Model):
    _name = 'genres.literature'
    _description = 'Genres of literature'

    name = fields.Char(string='Genres of literature', size=200, required=True)
