# -*- coding: utf-8 -*-
# from odoo import http


# class Custom-calendar(http.Controller):
#     @http.route('/custom-calendar/custom-calendar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-calendar/custom-calendar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-calendar.listing', {
#             'root': '/custom-calendar/custom-calendar',
#             'objects': http.request.env['custom-calendar.custom-calendar'].search([]),
#         })

#     @http.route('/custom-calendar/custom-calendar/objects/<model("custom-calendar.custom-calendar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-calendar.object', {
#             'object': obj
#         })
