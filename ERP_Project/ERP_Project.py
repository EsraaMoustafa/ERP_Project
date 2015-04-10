<<<<<<< HEAD
from openerp.osv import orm, fields

class erp_category(orm.Model):
    _name = 'erp.category'
    _columns = {
        'name': fields.char('الاسم',size=30),
        'code': fields.integer('رقم_الكود',size=50),
        'describtion': fields.text('الوصف'),
        'subcategory_id': fields.one2many('erp.subcategory','category_id','الاقسام')
=======
#! /usr/bin/env python
#encoding:UTF-8
import ERPProject
from openerp.osv import orm, fields
class erp_category(orm.Model):
    _name = 'erp.category'
    _columns = {
        'name': fields.char('name',size=30),
        'code': fields.integer('code',size=50),
        'description': fields.text('description'),
        'subcategory_id': fields.one2many('erp.subcategory','category_id','Cat')
>>>>>>> ed0d880b31dd5dcd0b1a3d95ac1109504d4f8ea7
    }

class erp_subcategory(orm.Model):
    _name = 'erp.subcategory'
    _columns = {
<<<<<<< HEAD
        'name': fields.char('الاسم',size=230),
        'code': fields.integer('رقم_الكود',size=50),
        'describtion': fields.text('الوصف'),
        'category_id': fields.many2one('erp.category','البوابة'),
        'subsubcategory': fields.one2many('erb.subsubcategory','subcategory','اقسام فرعية')
=======
        'name': fields.char('name',size=230),
        'code': fields.integer('code',size=50),
        'description': fields.text('description'),
        'category_id': fields.many2one('erp.category','Category'),
        'subsubcategory': fields.one2many('erb.subsubcategory','subcategory','Sub')
>>>>>>> ed0d880b31dd5dcd0b1a3d95ac1109504d4f8ea7
    }

class erp_subsubcategory(orm.Model):
    _name = 'erp.subsubcategory'
    _columns = {
<<<<<<< HEAD
        'name': fields.char('الاسم',size=30),
        'code': fields.integer('رقم_الكود',size=50),
        'describtion': fields.text('الوصف'),
        'subcategory': fields.many2one('erp.subcategory',' الفرعية  الاقسام')
=======
        'name': fields.char('name',size=30),
        'code': fields.integer('code',size=50),
        'description': fields.text('description'),
        'subcategory': fields.many2one('erp.subcategory','SubCat'),
	    'product_id': fields.one2many('pro.product','product','pro')

>>>>>>> ed0d880b31dd5dcd0b1a3d95ac1109504d4f8ea7
    }

