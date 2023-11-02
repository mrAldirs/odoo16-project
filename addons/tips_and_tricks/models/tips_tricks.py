from odoo import fields, models, api


class TipsTricks(models.Model):
    _name = 'tips.tricks'
    # _description = 'Description'

    name = fields.Char()
    number = fields.Integer()
    float_no = fields.Float(string='Float Number')
    document = fields.Binary()
    true = fields.Boolean(string='True?')
    image = fields.Image()
    date = fields.Date()
    date_time = fields.Datetime()
    yes_no = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='Yes or No')
    product_id = fields.Many2one('product.product')
    product_ids = fields.Many2many('product.product')
    tips_tricks_line_ids = fields.One2many('tips.tricks.line', 'tips_id')
    price = fields.Monetary()
    currency_id = fields.Many2one('res.currency')

class TipsTricksLine(models.Model):
    _name = 'tips.tricks.line'

    tips_id = fields.Many2one('tips.tricks')
    name = fields.Char()