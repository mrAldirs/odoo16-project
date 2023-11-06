# -*- coding: utf-8 -*-
# from odoo import http


# class OdOffice(http.Controller):
#     @http.route('/od_office/od_office', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/od_office/od_office/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('od_office.listing', {
#             'root': '/od_office/od_office',
#             'objects': http.request.env['od_office.od_office'].search([]),
#         })

#     @http.route('/od_office/od_office/objects/<model("od_office.od_office"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('od_office.object', {
#             'object': obj
#         })
