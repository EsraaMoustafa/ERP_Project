

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
