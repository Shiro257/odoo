# -*- coding: utf-8 -*-
# from odoo import http


# class F1(http.Controller):
#     @http.route('/f1/f1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/f1/f1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('f1.listing', {
#             'root': '/f1/f1',
#             'objects': http.request.env['f1.f1'].search([]),
#         })

#     @http.route('/f1/f1/objects/<model("f1.f1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('f1.object', {
#             'object': obj
#         })
