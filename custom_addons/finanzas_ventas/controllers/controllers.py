# -*- coding: utf-8 -*-
# from odoo import http


# class FinanzasVentas(http.Controller):
#     @http.route('/finanzas_ventas/finanzas_ventas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/finanzas_ventas/finanzas_ventas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('finanzas_ventas.listing', {
#             'root': '/finanzas_ventas/finanzas_ventas',
#             'objects': http.request.env['finanzas_ventas.finanzas_ventas'].search([]),
#         })

#     @http.route('/finanzas_ventas/finanzas_ventas/objects/<model("finanzas_ventas.finanzas_ventas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('finanzas_ventas.object', {
#             'object': obj
#         })

