from odoo import fields, models, api

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    fleet_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    dock_id = fields.Many2one('dock.model', string='Dock')
    category_id = fields.Many2one(related="fleet_id.category_id", readonly=False, store=True)
    total_weight = fields.Float(string="Weight", compute='_compute_weight', readonly=True, store=True)
    total_volume = fields.Float(string="Volume", compute='_compute_volume',readonly=True, store=True)

    @api.depends('category_id')
    def _compute_weight(self):
        for record in self:
            total = 0
            for move in record.move_ids:
                total += move.product_id.weight*move.product_qty
            if record.category_id or record.category_id.max_weight != 0 :
                record.total_weight = total*100 / record.category_id.max_weight
            else:
                record.total_weight = total;
            # if record.category or record.category_id.max_weight != 0 :
            #     record.total_weight = 100*sum(record.picking_ids.mapped('shipping_weight')) / record.category_id.max_weight
            # else: 
            #     record.total_weight = sum(record.picking_ids.mapped('shipping_weight'))

    @api.depends('category_id')
    def _compute_volume(self):
        for record in self:
            total = 0
            for move in record.move_ids:
                total += move.product_id.volume*move.product_qty
            if record.category_id or record.category_id.max_volume != 0 :
                record.total_volume = total*100 / record.category_id.max_volume
            else:
                record.total_volume = total;
