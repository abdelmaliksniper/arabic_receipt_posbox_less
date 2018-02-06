# -*- coding: utf-8 -*-
{
    'name': "Arabic POS Receipt using PosBoxLess",

    'summary': """ This module enables arabic printing for POS receipt Using Network Printer (PosBoxLess).
        """,

    'description': """
        
    """,

    'author': "Ad Mk Joseph",
    'website': "",
    'category': 'Generic Modules',
    'version': '1.0',
    'price': 350.0,
    'currency': 'EUR',
    'depends': ['point_of_sale'],


    'data': [
        'views/malik.xml',
        'views/malik_v.xml',
    ],
    'images': [
        'static/description/pos_receipt.png',
    ],

    'demo': [
        #'demo/demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
