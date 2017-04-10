{
    'name': "Sand Custom",

    'summary': """
        This module is used to customize the stock""",
    'description': """
        This module is used to customize the stock""",
    'version': '10.0.1.0.0',
    'application': True,
    'installable': True,
    'depends': ['product','stock'],
    'data': [
        "security/sand_security_view.xml",
        "views/main_sub_menu.xml",
        "views/product_template_view.xml",
        "views/stock_picking_views.xml",
    ],
    'demo': [],
    'qweb': [],
}
