from odoo import fields, models, api, _


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = 'mail.thread'
    _description = 'Doctor Record'
    _rec_name = 'ref'

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
                              string='Gender', tracking=True)
    ref = fields.Char(string='Reference', default=lambda self: _('New'))
    active = fields.Boolean(default=True)

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, f'{rec.ref} - {rec.name}'))
        return res

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.doctor')
        return super(HospitalDoctor, self).create(vals_list)