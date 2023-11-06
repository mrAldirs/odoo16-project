from odoo import fields, models, api, _
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _name = 'office.employee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Employee Record'
    _order = 'ref ASC'

    name = fields.Char(string='Name', required=True, tracking=True)
    nip = fields.Char(string='NIP', required=True, tracking=True)
    phone = fields.Char('Phone', tracking=True)
    address = fields.Text(string='Address', tracking=True)
    active = fields.Boolean(string='This Employee Active?', tracking=True)
    image = fields.Image(string='Profile', tracking=True)
    department = fields.Selection([
        ('accounting', 'Accounting'),
        ('computing', 'Computing'),
        ('management', 'Management')
    ], string='Department', tracking=True)
    dob = fields.Date(string='Date of Birth', tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    ref = fields.Char(string='Reference', default=lambda self: _('New'))
    note = fields.Text(string='Note', tracking=True)
    employee_lines = fields.One2many('office.employee.lines', 'employee_id', string='Employee Lines')
    position_id = fields.Many2one('office.position',string='Position', tracking=True)
    tag_ids = fields.Many2many('res.partner.category', 'office_employee_tag_rel',
                               'employee_id', 'tag_id', string='Tags')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('office.employee')
        return super(Employee, self).create(vals_list)

    @api.depends('dob')
    def _compute_age(self):
        self.age = False
        for rec in self:
            rec.age = relativedelta(date.today(), rec.dob).years

    def validation_constrains(self):
        today = fields.date.today()
        for rec in self:
            if rec.dob >= today:
                raise ValidationError(_('Invalid Date of Birth'))

class EmployeeLines(models.Model):
    _name = 'office.employee.lines'
    _description = 'Employee Lines'

    product_id = fields.Many2one('product.product', string='Product')
    product_qty = fields.Integer(string='Quantity')
    employee_id = fields.Many2one('office.employee', string='Employee ID')