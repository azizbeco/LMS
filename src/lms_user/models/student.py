from odoo import models,fields

class Student(models.Model):
    _name = "lu.student"
    _inherits = {'res.users': 'user_id'}

    user_id = fields.Many2one('res.users', required=True)
    company_id = fields.Many2one("res.company", string="Company")


