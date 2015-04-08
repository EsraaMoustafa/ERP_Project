#! /usr/bin/env python
#encoding:UTF-8
from openerp.osv import orm, fields

class erp_category(orm.Model):
    _name = 'erp.category'
    _columns = {
        'name': fields.char('الاسم',size=30),
        'code': fields.integer('رقم_الكود',size=50),
        'describtion': fields.text('الوصف'),
        'subcategory_id': fields.one2many('erp.subcategory','category_id','الاقسام')
    }

class erp_subcategory(orm.Model):
    _name = 'erp.subcategory'
    _columns = {
        'name': fields.char('الاسم',size=230),
        'code': fields.integer('رقم_الكود',size=50),
        'describtion': fields.text('الوصف'),
        'category_id': fields.many2one('erp.category','البوابة'),
        'subsubcategory': fields.one2many('erb.subsubcategory','subcategory','اقسام فرعية')
    }

class erp_subsubcategory(orm.Model):
    _name = 'erp.subsubcategory'
    _columns = {
        'name': fields.char('الاسم',size=30),
        'code': fields.integer('رقم_الكود',size=50),
        'describtion': fields.text('الوصف'),
        'subcategory': fields.many2one('erp.subcategory',' الفرعية  الاقسام')
    }

