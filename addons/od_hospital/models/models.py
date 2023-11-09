# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class od_hospital(models.Model):
#     _name = 'od_hospital.od_hospital'
#     _description = 'od_hospital.od_hospital'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
