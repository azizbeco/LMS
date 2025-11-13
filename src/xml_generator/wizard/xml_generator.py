from odoo import models, fields
import os

class XMLGenerate(models.TransientModel):
    _name = "xml.generate"
    _description = "XML Generate"

    module_path = fields.Char(string="Module path", required=True)
    model_ids = fields.Many2many("ir.model", string="Model", required=True)

    def generate(self):
        self.ensure_one()

        print("self.module_path:", self.module_path)
        print("self.model_ids:", self.model_ids)

        # required_fields = []
        for model in self.model_ids:
            for field in model.field_id.filtered(lambda x: x.required):
                print("field.name:", field.name)
                print("field.required:", field.required)
                # required_fields.append(field)

        views_path = os.path.join(self.module_path, "views")
        os.makedirs(views_path,exist_ok=True)
        file_path = os.path.join(views_path,f"{self.model_ids.name}.xml")

        xml_content = f"""
            <odoo>
                <data>
                    <record id="{ self.model_ids.name }_list" model="ir.ui.view">
                        <field name="name">{self.model_ids.name}</field>
                        <field name="model">{self.model_ids.name}</field>
                        <field name="arch" type="xml">
                            <list>
                                <field name="name"/>
                            </list>
                        </field>
                    </record>
                    <record id="{ self.model_ids.name }_form" model="ir.ui.view">
                        <field name="name">{self.model_ids.name}</field>
                        <field name="model">{self.model_ids.name}</field>
                        <field name="arch" type="xml">
                            <form>
                                <sheet>
                                    <group>
                                        <field name="name"/>
                                    </group>
                                </sheet>
                            </form>
                        </field>
                    </record>
            
                    <record id="{self.model_ids.name}_action" model="ir.actions.act_window">
                        <field name="name">{self.model_ids.name}</field>
                        <field name="res_model">{self.model_ids.name}</field>
                        <field name="view_mode">list,form</field>
                    </record>
            
                </data>
            </odoo>
        """

        with open(file_path, "w") as file:
            file.write(xml_content)

