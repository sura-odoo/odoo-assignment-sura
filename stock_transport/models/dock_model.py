from odoo import models, fields

class DockModel(models.Model):
    _name = "dock.model"
    _description = "Dock Model"

    name = fields.Char()
