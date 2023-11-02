# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tips_and_tricks(models.Model):
#     _name = 'tips_and_tricks.tips_and_tricks'
#     _description = 'tips_and_tricks.tips_and_tricks'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
