#! /usr/bin/env python
#encoding:UTF-8
from openerp.osv import orm, fields
class erp_category(orm.Model):
    _name = 'erp.category'
    _columns = {
        'name': fields.char('اسم الباب',size=30),
        'code': fields.integer('رقم الكود',size=50),
        'description': fields.text('الوصف'),
        'subcategory_id': fields.one2many('erp.subcategory','category_id','المجموعة')
    }

class erp_subcategory(orm.Model):
    _name = 'erp.subcategory'
    _columns = {
        'name': fields.char('اسم المجموعة',size=230),
        'code': fields.integer('رقم الكود',size=50),
        'description': fields.text('الوصف'),
        'category_id': fields.many2one('erp.category','الباب'),
        'subsubcategory': fields.one2many('erp.subsubcategory','subcategory','القسم')
    }

class erp_subsubcategory(orm.Model):
    _name = 'erp.subsubcategory'
    _columns = {
        'name': fields.char('اسم القسم',size=30),
        'code': fields.integer('رقم الكود',size=50),
        'description': fields.text('الوصف'),
        'subcategory': fields.many2one('erp.subcategory','المجموعة'),
	    'product_id': fields.one2many('pro.product','subsub_id','اسم المنتج')

    }

