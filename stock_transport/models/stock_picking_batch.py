from odoo import fields, models, api
from random import randint

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    fleet_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    dock_id = fields.Many2one('dock.model', string='Dock')
    category_id = fields.Many2one(related="fleet_id.category_id", readonly=False, store=True)
    total_weight = fields.Float(string="Weight", compute='_compute_weight', readonly=True, store=True)
    total_volume = fields.Float(string="Volume", compute='_compute_volume',readonly=True, store=True)
    count_transfer = fields.Integer(string="Transfer", compute='_compute_count_transfer', store=True)

    def _get_default_color(self):
        return randint(1, 11)

    color = fields.Integer('Color', default=_get_default_color, store=False)

    @api.depends('total_weight','total_volume')
    def _compute_display_name(self):
        super()._compute_display_name()
        for record in self:
            record.display_name = record.name+": "+str(record.total_weight)+", "+str(record.total_volume)

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

    @api.depends('move_line_ids')
    def _compute_count_transfer(self):
        for record in self:
            record.count_transfer = len(record.move_line_ids)
