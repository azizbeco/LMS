from tkinter.constants import CASCADE

from odoo import models, fields,api
from datetime import timedelta


class ScheduleTable(models.Model):
    _name = "le.schedule.table"
    _description = "Schedule Table"

    name = fields.Char(string="Name", required=True)
    group_id = fields.Many2one("le.group", string="Group", required=True)
    schedule_lesson_ids = fields.One2many("le.schedule.lesson", "schedule_table_id", string="Schedule Lessons",CASCADE="Ondelete")

    teacher_id = fields.Many2one("res.users", string="Teacher",)

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    weekday_ids = fields.Many2many("common.weekday", string="Weekdays")
    lesson_start_time = fields.Float(string="Start Time")
    lesson_end_time = fields.Float(string="End Time")

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            current_date = record.start_date
            lesson_weekdays = []
            for day in record.weekday_ids:
                lesson_weekdays.append(day.code)

            while current_date <= record.end_date:
                if current_date.weekday() in lesson_weekdays:
                    vals = {
                        'name': f"{current_date}",
                        'schedule_table_id': record.id,
                        'lesson_date':current_date,
                        'lesson_start_time':record.lesson_start_time,
                        'lesson_end_time':record.lesson_end_time
                    }
                    print(vals)
                    self.env["le.schedule.lesson"].create(vals)
                current_date += timedelta(days=1)
        return records

