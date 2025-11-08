from odoo import models, fields


class Course(models.Model):
    _name = "education.course"
    _description = "Course"

    name = fields.Char(string="Name", required=True)
    duration = fields.Float(string="Duration", required=True)
    duration_uom = fields.Many2one("uom.uom", required=True)
