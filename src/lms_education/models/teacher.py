from odoo import models,fields

class Teacher(models.Model):
    _inherit = "lu.teacher"

    schedule_table_ids = fields.One2many("le.schedule.table","teacher_id")
    schedule_table_lesson_ids = fields.One2many("le.schedule.lesson","teacher_id")