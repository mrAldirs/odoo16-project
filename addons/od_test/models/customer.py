from odoo import fields, models, api, _


class Customer(models.Model):
    _name = 'test.customer'
    _inherit = 'mail.thread'
    _description = 'Description of Customer'

    name = fields.Char(string='Name', tracking=True)
    customer_code = fields.Char(string='Code Customer', tracking=True)
    address = fields.Text(string='Address', tracking=True)
    npwp = fields.Char(string='NPWP', tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    mobile = fields.Char(string='Mobile', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    website = fields.Char(string='Website', tracking=True)
    tag_ids = fields.Many2many('res.partner.category', 'test_customer_tag_rel'
                               'customer_id', 'tag_id', string='Tags', tracking=True)
    attachment_ids = fields.One2many('test.attachment', 'customer_id', string='Attachments')
    note = fields.Text(string='Notes', tracking=True)
    ref = fields.Char(string='Ref', default=lambda self: _('New'))
    company = fields.Char(string='Company', tracking=True)
    image = fields.Image(string='Profile', tracking=True)

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, f'{rec.name}'))
        return res

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('test.customer')
        return super(Customer, self).create(vals_list)

    def action_open_attachment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Attachment',
            'res_model': 'test.attachment',
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {
                'default_customer_id': self.id
            }
        }