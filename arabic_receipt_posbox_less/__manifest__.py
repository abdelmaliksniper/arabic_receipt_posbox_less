# -*- coding: utf-8 -*-
{
    'name': "Arabic POS Receipt using PosBoxLess",

    'summary': """ This module enables arabic printing for POS receipt Using Network Printer (PosBoxLess).
        """,

    'description': """
        
    """,

    'author': "Abdelmalik Yousif",
    'website': "abdelmalik19930@gmail.com",
    'category': 'Generic Modules',
    'version': '1.0',
    'price': 199.0,
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
