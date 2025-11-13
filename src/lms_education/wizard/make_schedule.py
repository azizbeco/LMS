from odoo import models,fields,api

class MakeSchedule(models.TransientModel):
    _name = "le.education.group.schedule.wizard"
    _description = "Make Schedule"

    group_id = fields.Many2one("le.group",string="Group",readonly=True)

    weekday_ids = fields.Many2many("common.weekday",string="Weekday")


    name = fields.Char(string="name",required=True)
    start_date = fields.Date(string="Start Date",required=True)
    end_date = fields.Date(string="End Date",required=True)
    lesson_start_time = fields.Float(string="lesson_start_time",required=True)
    lesson_end_time = fields.Float(string="lesson_end_time",required=True)


    def make_schedule(self):
        for record in self:
            if not record.weekday_ids.ids:
                raise ValueError("Choice Weekday")

            vals = {
                'name':record.name,
                'group_id':record.group_id.id,
                'start_date':record.start_date,
                'end_date':record.end_date,
                'weekday_ids':record.weekday_ids.ids,
                'lesson_start_time':record.lesson_start_time,
                'lesson_end_time':record.lesson_end_time,

            }
            self.env["le.schedule.table"].create(vals)
            #





