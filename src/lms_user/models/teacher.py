from odoo import models,fields,api

class Teachers(models.Model):
    _name = "lu.teacher"
    _inherit = ["lu.worker.info"]
    _inherits = {'res.users':'user_id'}

    user_id = fields.Many2one('res.users',required=True)
    company_id = fields.Many2one("res.company", string="Company")

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for record in vals_list:
    #         record["user_type"] = "teacher"
    #
    #     return super().create(vals_list)