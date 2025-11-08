from odoo import models, fields


class Payment(models.Model):
    _name = "payment.payment"
    _description = "Payment"

    user_id = fields.Many2one("res.users", string="User")
    amount = fields.Float(string="Amount")
