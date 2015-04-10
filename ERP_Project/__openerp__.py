<<<<<<< HEAD
{
    'name': 'نظام إدارة المخازن',
    'version': '1.0',
    'summary': 'anything',
    'auther': 'ITI',
    'description': "ay7aga",
    'website': 'http://www.iti.gov.eg',
    'depends': ['base', 'hr'],
    'data': ['ERP_Project_view.xml', 'ERPProject_view.xml','workflow.xml', 'security/odoowarehouse_security.xml',
             'security/ir.model.access.csv'],
    'installed': True,
    'auto-install': False,
}
=======
<<<<<<< HEAD
{
    'name':'stockee',
    'version':'1.1',
    'summary': 'برنامج ادارة جميع المخازن',
    'description': """
    يساعد هذا البرنامج لتسهيل عملية ادارة جميع المخازن
    """ ,
    'author':'طلاب معد تكنولوجيا المعلومات',
    'depends':['base'],
    'data': [
        'ERP_Project_view.xml',
    ],
    'installable':'true',

}
=======


{
    'name':'OurStocks', #the name of module
    'version':'1.1',
    'summary':'',
    'auther':'ITI',
    'description':"""""",
    'website':'http://www.iti.gov.eg',
    'depends':['base','hr','report_webkit'],
    'data':['ERPProject_view.xml','ERP_Project_view.xml','reportproduct/report.xml','reportmystock/report.xml',
		'security/ERP_Project_security.xml','security/ir.model.access.csv'], #xml files
    'installed':True, #ynf3 eno ytstab
    'auto-install':False, #ytstab mno l nafso
}
>>>>>>> ed0d880b31dd5dcd0b1a3d95ac1109504d4f8ea7
>>>>>>> 74e071feb1cd591d6da3c18675d1507050498672
