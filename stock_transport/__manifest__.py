{
    'name': "Stock Transport",
    'version': '1.0',
    'depends': ['stock_picking_batch','fleet'],
    'author': "Suyash Rajput",
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_category_inherit.xml',
        'views/stock_picking_batch_inherit.xml',
        'views/stock_picking_views_inherit.xml'
    ],
    "demo": [],
    'license': 'LGPL-3',
}
