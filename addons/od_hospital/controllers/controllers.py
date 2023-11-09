# -*- coding: utf-8 -*-
# from odoo import http


# class OdHospital(http.Controller):
#     @http.route('/od_hospital/od_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/od_hospital/od_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('od_hospital.listing', {
#             'root': '/od_hospital/od_hospital',
#             'objects': http.request.env['od_hospital.od_hospital'].search([]),
#         })

#     @http.route('/od_hospital/od_hospital/objects/<model("od_hospital.od_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('od_hospital.object', {
#             'object': obj
#         })
