#! /usr/bin/env python
#encoding:UTF-8
from openerp.osv import orm, fields
class erp_category(orm.Model):
    _name = 'erp.category'
    _columns = {
        'name': fields.char('name',size=30),
        'code': fields.integer('code',size=50),
        'description': fields.text('description'),
        'subcategory_id': fields.one2many('erp.subcategory','category_id','Cat')
    }

class erp_subcategory(orm.Model):
    _name = 'erp.subcategory'
    _columns = {
        'name': fields.char('name',size=230),
        'code': fields.integer('code',size=50),
        'description': fields.text('description'),
        'category_id': fields.many2one('erp.category','Category'),
        'subsubcategory': fields.one2many('erp.subsubcategory','subcategory','Sub')
    }

class erp_subsubcategory(orm.Model):
    _name = 'erp.subsubcategory'
    _columns = {
        'name': fields.char('name',size=30),
        'code': fields.integer('code',size=50),
        'description': fields.text('description'),
        'subcategory': fields.many2one('erp.subcategory','SubCat'),
	    'product_id': fields.one2many('pro.product','subsub_id','pro')

    }

