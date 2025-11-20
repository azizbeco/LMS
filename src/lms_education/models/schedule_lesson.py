from email.policy import default

from odoo import models, fields,api
from datetime import timedelta

from odoo.api import ondelete


class ScheduleLesson(models.Model):
    _name = "le.schedule.lesson"
    _description = "Schedule Lesson"

    name = fields.Char(string="Name", required=True)
    schedule_table_id = fields.Many2one("le.schedule.table", string="Schedule",ondelete="cascade")
    teacher_id = fields.Many2one("lu.teacher",string="Teacher")

    lesson_date = fields.Date(string="Lesson Date", required=True)
    lesson_start_time = fields.Float(string="Start Time", required=True)
    lesson_end_time = fields.Float(string="End Time", required=True)
    next_lesson_date = fields.Date(string="Next Lesson Date")

    skip_or_move_lesson = fields.Selection([
        ('skip','Skip Lesson'),
        ('move','Move Lesson'),
    ],default="skip")

    skip_lesson_date = fields.Date(string="Lesson Date")
    skip_lesson_start_time = fields.Float(string="Start Time")
    skip_lesson_end_time = fields.Float(string="End Time")

    def schedule_lesson_move_button(self):
        return {
            'type':'ir.actions.act_window',
            'name':f'{self.name} lesson',
            'res_model':'le.schedule.lesson',
            'view_mode':'form',
            'target':'new',
            'view_id':self.env.ref('lms_education.move_schedule_lesson_form').id,
            'context':{
                'default_name': self.name,
                'default_lesson_date': self.lesson_date,
                'default_schedule_table_id': self.schedule_table_id,
                'default_lesson_start_time': self.lesson_start_time,
                'default_lesson_end_time': self.lesson_end_time,
            }
        }

    def skip_schedule_lesson(self):
        for record in self:
            record.sudo().write({
                'lesson_date': record.skip_lesson_date,
                'lesson_start_time': record.skip_lesson_start_time,
                'lesson_end_time': record.skip_lesson_end_time,
            })


    def move_schedule_lesson(self):
        return None
        # for record in self:
        #     current_date = record.lesson_date
        #     # old_lesson_date = " "
        #
        #     lesson_weekdays = []
        #     for day in record.schedule_table_id.weekday_ids:
        #         lesson_weekdays.append(day.code)
        #
        #
        #     lessons = record.schedule_table_id.group_id.course_id.lesson_ids
        #     total_lessons = len(lessons)
        #     lesson_index = 0
        #
        #     # lessons = self.env["le.schedule.lesson"].search([
        #     #     ('lesson_date', '>', record.lesson_date)
        #     # ], order="lesson_date asc")
        #     # print(lessons)
        #     #
        #     # for lesson in lessons:
        #
        #
        #     while True:
        #         current_date += timedelta(days=1)
        #         if current_date.weekday() in lesson_weekdays:
        #
        #             vals = {
        #                 'name':record.name,
        #                 'lesson_date':current_date,
        #             }
        #
        #             self.write(vals)
        #
        #         lesson = self.env["le.schedule.lesson"].search([],order="id desc",limit=1)
        #
        #         if current_date > lesson.lesson_date:
        #             break
        #         current_date += timedelta(days=1)


            # for lesson in range(lesson_index,total_lessons):
            #     if current_date.weekday() in lesson_weekdays:
            #         # lesson = lessons[lesson_index]
            #         # old_lesson_date = current_date
            #
            #         lesson.write({
            #             'name':record.name,
            #             'lesson_date':current_date,
            #         })
            #         # self.env["le.schedule.lesson"].write(vals)
            #         lesson_index +=1
            #
            #         current_date += timedelta(days=1)





    @api.constrains("lesson_start_time", "lesson_end_time", "lesson_date", "teacher_id")
    def _check_conflict(self):
        """
        Joriy dars kuni joriy o'qituvchiga dars vaqti konflikt bo'lib qolmasligi tekshirildi
        """

        for record in self:
            if self.env["le.schedule.lesson"].sudo().search_count([
                "&",
                ("lesson_date", "=", record.lesson_date),
                "&",
                ("teacher_id", "=", record.teacher_id.id),
                "|",
                "&",
                ("lesson_start_time", "<", record.lesson_start_time),
                ("lesson_end_time", ">", record.lesson_start_time),
                "&",
                ("lesson_start_time", "<", record.lesson_end_time),
                ("lesson_end_time", ">", record.lesson_end_time),
            ]) > 0:
                raise ValueError("Lesson Conflict")






            # while current_date <= record.schedule_table_id.end_date and lesson_index < total_lessons:
