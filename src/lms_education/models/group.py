from odoo import models, fields


class Group(models.Model):
    """
    FSWD - 1
    """
    _name = "le.group"
    _description = "Group"

    group_student_ids = fields.One2many("le.group.student","group_id")
    course_id = fields.Many2one("le.course", string="Course", required=True,ondelete="cascade")
    schedule_table_ids = fields.One2many("le.schedule.table","group_id")
    name = fields.Char(string="Name", required=True)



    def make_schedule_wizard(self):
        return {
            'type':'ir.actions.act_window',
            'name':'Make Schedule',
            'res_model':'le.education.group.schedule.wizard',
            'view_mode':'form',
            'target':'new',
            'context':{'default_group_id':self.id}
        }
