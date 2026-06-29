# -*- coding: utf-8 -*-
{
    'name': "finanzas_ventas",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/Producto/producto_R_menu.xml',
        'views/Producto/producto_action.xml',
        'views/Producto/producto_C_U_view.xml',
        'views/Cierre/cierre_C_U_view.xml',
        'views/Cierre/cierre_action.xml',
        
    
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

