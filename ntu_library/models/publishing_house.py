from odoo import fields, models


class PublishingHouse(models.Model):
    _name = 'publishing.house'
    _description = 'Publishing house'

    name = fields.Char(string='Publishing house', size=150, required=True)
    description = fields.Text()
