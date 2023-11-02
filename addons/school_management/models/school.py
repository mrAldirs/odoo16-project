from odoo import fields, models, api, _
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class School(models.Model):
    _name = 'school.student'
    # _description = 'Description'

    name = fields.Many2one('res.partner', string='Student')
    address = fields.Char(string='Address')
    class_id = fields.Integer(string='Class')
    division = fields.Char(string='Division')
    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age')
    admin_date = fields.Date(string='Admin Date', default=fields.date.today())
    officer_id = fields.Many2one('res.users', string='Officer', default=lambda self:self.env.user)

    @api.onchange('name')
    def _onchange_name(self):
        self.address = self.name.street

    @api.depends('dob')
    def _compute_age(self):
        self.age = False
        for rec in self:
            rec.age = relativedelta(date.today(), rec.dob).years

    @api.constrains('dob')
    def validation_constrains(self):
        today = fields.date.today()
        for rec in self:
            if rec.dob >= today:
                raise ValidationError(_('Invalid Date of Birth'))
            elif (rec.class_id > 12) or (rec.class_id < 1):
                raise ValidationError(_('Invalid Class'))