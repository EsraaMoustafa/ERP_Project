#! /usr/bin/env python
<<<<<<< HEAD
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
        self.write(cr, uid, ids, {'state': 'managerConfirm'})
        return True


    def product_in_stock(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'inStock'})
        return True







class pro_supplier(orm.Model):
    _name = 'pro.supplier'
    _columns = {
        'name' : fields.char(string = 'اسم المورد'),
        'address' : fields.char(string = 'عنوان المورد'),
        'tel' : fields.char(string = 'رقم التليفون'),
        'pro_id': fields.many2one('pro.product', 'المنتج')
    }

class res_users(osv.osv):
    _inherit = "res.users"
    _name = "res.users"
    _columns = {
        'stock_id': fields.one2many('my.stock','keeper_id',string='المخزن'),
    }


class my_stock(orm.Model):
    _name = 'my.stock'

    _columns = {
      'keeper_id':fields.many2one('res.users',
      string='Keeper',required=True),
      }
=======
#encoding:UTF-8
import ERP_Project
from openerp.osv import orm, fields
class pro_product(orm.Model):
    status = [('new','new'),('reused','reused'),('damaged','damaged')]
    _name = 'pro.product'
    _columns = {
        'code' : fields.integer(string='code'),
        'name' : fields.char(string='name',size=50),
        'status' : fields.selection(status,'status'),
        'quantity' : fields.integer(string='quantity'),
        'price' : fields.integer(string='price'),
        'description' : fields.char(string='description',size=250),
	    'product': fields.many2one('erp.subsubcategory',
                                   'pro')
    }
>>>>>>> 74e071feb1cd591d6da3c18675d1507050498672
