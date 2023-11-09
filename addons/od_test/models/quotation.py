from odoo import fields, models, api, _


class Quotation(models.Model):
    _name = 'test.quotation'
    _inherit = 'mail.thread'
    _description = 'Quotations Record'

    name = fields.Many2one('test.customer',string='Customer', tracking=True)
    code = fields.Char(string='Code Customer', related='name.customer_code', tracking=True)
    expiration = fields.Date(string='Expiration', tracking=True)
    quot_date = fields.Date(string='Quotation Date', tracking=True)
    price_list = fields.Many2one('product.pricelist', string='Pricelist', tracking=True)
    ref = fields.Char(string='Reference', default=lambda self: _('New'))
    quotation_lines = fields.One2many('test.quotation.lines', 'quotation_id', string='Quotation Lines')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('test.quotation')
        return super(Quotation, self).create(vals_list)

class QuotationLines(models.Model):
    _name = 'test.quotation.lines'
    _description = 'Quotation Lines'

    product_id = fields.Many2one('product.product', string='Product')
    product_qty = fields.Integer(string='Quantity')
    quotation_id = fields.Many2one('test.quotation', string='Quotation ID')