from odoo import models,fields

class Student(models.Model):
    _inherit = "lu.student"

    group_ids = fields.One2many("le.group.student","student_id")

