# -*- coding: utf-8 -*-
# from odoo import http


# class XmlGenerator(http.Controller):
#     @http.route('/xml_generator/xml_generator', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xml_generator/xml_generator/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('xml_generator.listing', {
#             'root': '/xml_generator/xml_generator',
#             'objects': http.request.env['xml_generator.xml_generator'].search([]),
#         })

#     @http.route('/xml_generator/xml_generator/objects/<model("xml_generator.xml_generator"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xml_generator.object', {
#             'object': obj
#         })

