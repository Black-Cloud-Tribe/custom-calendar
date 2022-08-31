# -*- coding: utf-8 -*-
{
    'name': "custom-calendar",

    'summary': """
        Adds new functionalities to Calendar module (As validations)
        """,


    'author': "Black CLoud Tribe",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Calendar',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','calendar'],

    # always loaded
    'data': [
        
        'views/custom_calendar_event.xml'
    ],
    "installable": True,
    "development_status": "Beta",
}
