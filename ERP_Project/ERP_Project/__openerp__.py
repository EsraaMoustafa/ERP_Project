#! /usr/bin/env python
#encoding:UTF-8
{
    'name':'stockee',
    'version':'1.1',
    'summary': 'برنامج ادارة جميع المخازن',
    'description': """
    يساعد هذا البرنامج لتسهيل عملية ادارة جميع المخازن
    """ ,
    'author':'طلاب معد تكنولوجيا المعلومات',
    'depends':['base','hr',],
    'data': [
        'ERP_Project_view.xml',
        'security/ERP_Project_security.xml',
        'security/ir.model.access.csv',
        # 'report/report.xml'
    ],
    'installable': True,
    'auto_install': False,

}
