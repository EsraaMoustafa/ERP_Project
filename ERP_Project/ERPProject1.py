#! /usr/bin/env python
# encoding:UTF-8
from openerp.osv import orm,osv, fields


class pro_product(orm.Model):
    status = [('new', 'new'), ('reused', 'reused'), ('damaged', 'damaged')]
    _name = 'pro.product'
    _columns = {
        'code': fields.integer(string='code'),
        'name': fields.char(string='name', size=50),
        'status': fields.selection(status, 'status'),
        'quantity': fields.integer(string='quantity'),
        'price': fields.integer(string='price'),
        'description': fields.char(string='description', size=250),
        'subsub_id': fields.many2one('erp.subsubcategory', 'pro'),
        'stockk_id': fields.many2one('my.stock', 'stock'),

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