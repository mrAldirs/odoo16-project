# -*- coding: utf-8 -*-
{
    'name': "od_test",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','mail','product'],

    # always loaded'data/sequence.xml',
    #         'views/views.xml',
    #         'views/templates.xml',
    #         'views/menu.xml',
    #         'views/quotation.xml',
    #         'views/customer.xml',
    #         'views/attachment.xml'
    #     ],
    #     # only loaded in demonstration
    'data': [
        'security/ir.model.access.csv',
        mode
    'demo': [
        'demo/demo.xml',
    ],
}
