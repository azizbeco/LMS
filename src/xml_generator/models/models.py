# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class xml_generator(models.Model):
#     _name = 'xml_generator.xml_generator'
#     _description = 'xml_generator.xml_generator'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

