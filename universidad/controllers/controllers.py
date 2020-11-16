# -*- coding: utf-8 -*-
# from odoo import http


# class Universidad(http.Controller):
#     @http.route('/universidad/universidad/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/universidad/universidad/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('universidad.listing', {
#             'root': '/universidad/universidad',
#             'objects': http.request.env['universidad.universidad'].search([]),
#         })

#     @http.route('/universidad/universidad/objects/<model("universidad.universidad"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('universidad.object', {
#             'object': obj
#         })
