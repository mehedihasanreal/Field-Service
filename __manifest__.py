# -*- coding: utf-8 -*-

{
    'name': 'Field Service Automation',
    'version': '1.0.0',
    'category': 'service',
    'author': 'Unisoft System Ltd',
    'summary': ' Field Service Automation',
    'description': 'Field Service Automation',
    'sequence': -200,
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/menu.xml',
        'views/field_service_view.xml',
        'views/field_service_data_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

}
