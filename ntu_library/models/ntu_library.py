from odoo import _, api, fields, models


class NTULibrary(models.Model):
    _name = 'ntu.library'
    _description = 'NTU Library'

    name = fields.Char(string='Book name', size=200, required=True)
    autor = fields.Many2one('ntu.library.autor', string='Autor', required=True)
    language = fields.Many2one('ntu.library.lang', string='Language')
    genres_of_literature = fields.Many2many('genres.literature', string='Genres of literature', required=True)
    publishing_house = fields.Many2one('publishing.house', string='Publishing house', required=True)
    year_of_publication = fields.Integer(string='Year of publication')
    partner_id = fields.Many2one('res.partner', string='Reader')
    reservation = fields.Boolean()
    description = fields.Text()
