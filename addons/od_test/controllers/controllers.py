# -*- coding: utf-8 -*-
# from odoo import http


# class OdTest(http.Controller):
#     @http.route('/od_test/od_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/od_test/od_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('od_test.listing', {
#             'root': '/od_test/od_test',
#             'objects': http.request.env['od_test.od_test'].search([]),
#         })

#     @http.route('/od_test/od_test/objects/<model("od_test.od_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('od_test.object', {
#             'object': obj
#         })
