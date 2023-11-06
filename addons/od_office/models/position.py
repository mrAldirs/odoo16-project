from odoo import fields, models, api, _


class Position(models.Model):
    _name = 'office.position'
    _inherit = 'mail.thread'
    _description = 'Description of position'
    _rec_name = 'ref'

    name = fields.Char(string='Name', required=True, tracking=True)
    ref = fields.Char(string='Ref', default=lambda self: _('New'))

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, f'{rec.name}'))
        return res

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('office.position')
        return super(Position, self).create(vals_list)