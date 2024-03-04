from odoo import models, fields, api

class FleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float()
    max_volume = fields.Float()

    def _compute_display_name(self):
        super()._compute_display_name()
        for record in self:
            record.display_name = record.name+" ("+str(record.max_weight)+", "+str(record.max_volume)+")"
