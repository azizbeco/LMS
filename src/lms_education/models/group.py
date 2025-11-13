from odoo import models, fields


class Group(models.Model):
    """
    FSWD - 1
    """
    _name = "le.group"
    _description = "Group"

    name = fields.Char(string="Name", required=True)
    course_id = fields.Many2one("le.course", string="Course", required=True)


    def make_schedule_wizard(self):
        return {
            'type':'ir.actions.act_window',
            'name':'Make Schedule',
            'res_model':'le.education.group.schedule.wizard',
            'view_mode':'form',
            'target':'new',
            'context':{'default_group_id':self.id}
        }
