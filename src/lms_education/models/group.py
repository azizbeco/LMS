from email.policy import default

from odoo import models, fields


class Group(models.Model):
    """
    FSWD - 1
    """
    _name = "le.group"
    _description = "Group"

    group_student_ids = fields.One2many("le.group.student","group_id")
    course_id = fields.Many2one("le.course", string="Course", required=True)
    schedule_table_ids = fields.One2many("le.schedule.table","group_id")
    name = fields.Char(string="Name", required=True)

    # active = fields.Boolean(default=False)


    def make_schedule(self):
        return {
            'type':'ir.actions.act_window',
            'name':'Make Schedule',
            'res_model':'le.schedule.table',
            'view_mode':'form',
            'target':'new',
            'view_id':self.env.ref('lms_education.schedule_table_group_form').id,
            'context':{'default_group_id':self.id}
        }
