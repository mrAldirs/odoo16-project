from odoo import fields, models, api


class Attachment(models.Model):
    _name = 'test.attachment'
    _description = 'Description for Attachment'

    name = fields.Char(string='Name')
    url = fields.Char(string='URL')
    customer_id = fields.Many2one('test.customer', string='Customer ID')