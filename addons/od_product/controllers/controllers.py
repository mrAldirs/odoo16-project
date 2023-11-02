# -*- coding: utf-8 -*-
# from odoo import http


# class OdProduct(http.Controller):
#     @http.route('/od_product/od_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/od_product/od_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('od_product.listing', {
#             'root': '/od_product/od_product',
#             'objects': http.request.env['od_product.od_product'].search([]),
#         })

#     @http.route('/od_product/od_product/objects/<model("od_product.od_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('od_product.object', {
#             'object': obj
#         })
