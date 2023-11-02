# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class od_openacademy(models.Model):
#     _name = 'od_openacademy.od_openacademy'
#     _description = 'od_openacademy.od_openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
