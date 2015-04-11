#! /usr/bin/env python
# encoding:UTF-8

from openerp.osv import orm,osv, fields

class pro_product(orm.Model):
    def codeConcat(self, cr, uid, ids , name , arg , context=None):
        result = {}
        ids = self.search(cr, uid, [])
        products = self.browse(cr, uid, ids , context)
        for product in products:
            result[product.id]=str(product.code)+str(product.subsub_id.code)+str(product.sub_id.code)+str(product.cat_id.code)
        return result
    status = [('new', 'جديد'), ('reused', 'مستعمل'), ('damaged', 'تالف')]
    stage = [('new','جديد') , ('recieved','مستلم') , ('underReview', 'تحت الفحص') , ('approved','معتمد') , ('keeperConfirm', 'موافقة أمين المخزن') ,('managerConfirm','موافقة مدير المخزن'),('inStock','في المخزن')]
    _name = 'pro.product'
    _columns = {
        'code': fields.integer(string='رقم الكود'),
        'name': fields.char(string='اسم المنتج', size=50),
        'status': fields.selection(status, 'الحالة'),
        'quantity': fields.integer(string='الكمية'),
        'price': fields.integer(string='السعر'),
        'description': fields.text(string='الوصف', size=250),
        'cat_id' : fields.many2one('erp.category','الباب'),
        'sub_id' : fields.many2one('erp.subcategory','المجموعة'),
        'subsub_id': fields.many2one('erp.subsubcategory', 'القسم'),
        'stockk_id': fields.many2one('my.stock', 'المخزن'),
        'concat' :fields.function(codeConcat, string='الكود كامل', method=True, type='char', store=True),
        'stage':fields.selection(stage, 'المرحلة',readonly=True)

    }



    def product_new(self, cr, uid, ids):
        self.write(cr, uid, ids, {'stage': 'new'})
        return True


    def product_recieved(self, cr, uid, ids):
         self.write(cr, uid, ids, {'stage': 'recieved'})
         return True


    def product_underReview(self, cr, uid, ids):
        self.write(cr, uid, ids, {'stage': 'underReview'})
        return True


    def product_approved(self, cr, uid, ids):
        self.write(cr, uid, ids, {'stage': 'approved'})
        return True


    def product_keeper_confirm(self, cr, uid, ids):
        self.write(cr, uid, ids, {'stage': 'keeperConfirm'})
        return True


    def product_manager_confirm(self, cr, uid, ids):
        self.write(cr, uid, ids, {'stage': 'managerConfirm'})
        return True


    def product_in_stock(self, cr, uid, ids):
        self.write(cr, uid, ids, {'stage': 'inStock'})
        return True



class pro_supplier(orm.Model):
    _name = 'pro.supplier'
    _columns = {
        'name' : fields.char(string = 'اسم المورد'),
        'address' : fields.char(string = 'عنوان المورد'),
        'tel' : fields.char(string = 'رقم التليفون'),
        'pro_id': fields.many2one('pro.product', 'المنتج')
    }



class search_product(orm.Model):
    _name = 'search.product'
    ch = [('name','الإسم'), ('code','رقم الكود')]
    _columns = {
        'search': fields.char(string='بحث',size=100),
        'change': fields.selection(ch,string='بحث من خلال',size=100),
        'result': fields.text(string='النتائج',size=500)
    }
    def func1(self, cr, uid, ids, search , change , context=None):
        record = self.pool.get('pro.product').search(cr, uid, [(change,'=',search)], context=context)
        record=self.pool.get('pro.product').read(cr, uid,record , context=context)
        if record:
            v = {'result': 'الإسم:'+str(record[0]['name'])+',الحالة:'+str(record[0]['status'])
                           +',الكود:'+str(record[0]['code'])
                 +',الكمية:'+str(record[0]['quantity'])+',السعر:'+str(record[0]['price'])
                 +',الوصف:'+str(record[0]['description'])
                 }
        else:
            v = {'result': ''}
        return {'value':v}


class res_users(osv.osv):
    _inherit = "res.users"
    _name = "res.users"
    _columns = {
        'stock_id': fields.one2many('my.stock','keeper_id',string='المخزن'),
    }

    def chusergroup(self, cr, uid, ids, context=None):
        pass




class my_stock(orm.Model):
    _name = 'my.stock'

    _columns = {
      'address': fields.char(string='العنوان',size=100),
      'name':fields.char(string='الإسم',size=100),
      'keeper_id':fields.many2one('res.users',
      string='أمين المخزن',required=True),
      }