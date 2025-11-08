from odoo import models, fields


class WorkerInfo(models.AbstractModel):
    _name = "user_management.worker.info"
    _description = "Worker Info"

    experience_years = fields.Integer()
    worked_places = fields.Text()
