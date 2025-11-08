from odoo import models, fields


class XMLGenerate(models.TransientModel):
    _name = "xml.generate"
    _description = "XML Generate"

    module_path = fields.Char(string="Module", required=True)
    model_ids = fields.Many2many("ir.model", string="Model", required=True)

    def generate(self):
        self.ensure_one()

        print("self.module_path:", self.module_path)
        print("self.model_ids:", self.model_ids)

        for model in self.model_ids:
            for field in model.field_id.filtered(lambda x: x.required):
                print("field.name:", field.name)
                print("field.required:", field.required)
