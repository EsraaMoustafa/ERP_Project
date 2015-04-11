#! /usr/bin/env python
# encoding:UTF-8

from openerp.osv import orm, osv, fields


class pro_product(orm.Model):
    def check_keeper(self, cr, uid, ids, is_keeper, arg, context):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            keeper_id = product.stokk_id.keeper_id.id
            res[product.id] = (keeper_id == uid)
        return res

    def check_kmanager(self, cr, uid, ids, is_kmanager, arg, context):
        group = self.pool.get('res_groups').search(cr, uid, [('name', '=', 'مدير مخزن')], context=context)
        uidd=self.pool.get('res_groups_users_rel').browse(cr, uid, [('gid', '=', group)], context=context)[0]['uid']
        return uidd == uid

    def check_smanager(self, cr, uid, ids, is_smanager, arg, context):
        group = self.pool.get('res_groups').search(cr, uid, [('name', '=', 'مدير المخازن')], context=context)
        uidd=self.pool.get('res_groups_users_rel').browse(cr, uid, [('gid', '=', group)], context=context)[0]['uid']
        return uidd == uid

    def check_committee(self, cr, uid, ids, is_committee, arg, context):
        group = self.pool.get('res_groups').search(cr, uid, [('name', '=', 'عضو من اعضاء اللجنة')], context=context)
        uidd=self.pool.get('res_groups_users_rel').browse(cr, uid, [('gid', '=', group)], context=context)[0]['uid']
        return uidd == uid

    def codeConcat(self, cr, uid, ids, code, arg, context=None):
        result = {}
        ids = self.search(cr, uid, [])
        products = self.browse(cr, uid, ids, context)
        for product in products:
            result[product.id] = str(product.code) + str(product.subsub_id.code) + str(product.sub_id.code) + str(
                product.cat_id.code)
        return result

    status = [('new', 'جديد'), ('reused', 'مستعمل'), ('damaged', 'تالف')]
    stage = [('new', 'جديد'), ('recieved', 'مستلم'), ('underReview', 'تحت الفحص'), ('approved', 'معتمد'),
             ('keeperConfirm', 'موافقة أمين المخزن'), ('managerConfirm', 'موافقة مدير المخزن'),
             ('inStock', 'في المخزن')]
    _name = 'pro.product'
    _columns = {
        'code': fields.integer(string='رقم الكود'),
        'name': fields.char(string='اسم المنتج', size=50),
        'status': fields.selection(status, 'الحالة'),
        'quantity': fields.integer(string='الكمية'),
        'price': fields.integer(string='السعر'),
        'description': fields.text(string='الوصف', size=250),
        'cat_id': fields.many2one('erp.category', 'الباب'),
        'sub_id': fields.many2one('erp.subcategory', 'المجموعة'),
        'subsub_id': fields.many2one('erp.subsubcategory', 'القسم'),
        'stockk_id': fields.many2one('my.stock', 'المخزن'),
        'concat': fields.function(codeConcat, string='الكود كامل', method=True, type='char', store=True),
        'stage': fields.selection(stage, 'المرحلة', readonly=True),
        'is_keeper': fields.function(check_keeper, type='boolean', store=False),
        'is_kmanager': fields.function(check_kmanager, type='boolean', store=False),
        'is_smanager': fields.function(check_smanager, type='boolean', store=False),
        'is_committee': fields.function(check_committee, type='boolean', store=False),

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
        'name': fields.char(string='اسم المورد'),
        'address': fields.char(string='عنوان المورد'),
        'tel': fields.char(string='رقم التليفون'),
        'pro_id': fields.many2one('pro.product', 'المنتج')
    }


class search_product(orm.Model):
    _name = 'search.product'
    ch = [('name', 'الإسم'), ('code', 'رقم الكود')]
    _columns = {
        'search': fields.char(string='بحث', size=100),
        'change': fields.selection(ch, string='بحث من خلال', size=100),
        'result': fields.text(string='النتائج', size=500)
    }

    def func1(self, cr, uid, ids, search, change, context=None):
        record = self.pool.get('pro.product').search(cr, uid, [(change, '=', search)], context=context)
        record = self.pool.get('pro.product').read(cr, uid, record, context=context)
        if record:
            v = {'result': 'الإسم:' + str(record[0]['name']) + ',الحالة:' + str(record[0]['status'])
                           + ',الكود:' + str(record[0]['code'])
                           + ',الكمية:' + str(record[0]['quantity']) + ',السعر:' + str(record[0]['price'])
                           + ',الوصف:' + str(record[0]['description'])
                 }
        else:
            v = {'result': ''}
        return {'value': v}


class res_users(orm.Model):
    _inherit = "res.users"
    _name = "res.users"
    _columns = {
        'stock_id': fields.one2many('my.stock', 'keeper_id', string='المخزن'),
    }


class res_groups(orm.Model):
    _inherit = "res.groups"
    _name = "res.groups"
    _columns = {
    }


class my_stock(orm.Model):
    _name = 'my.stock'

    _columns = {
        'address': fields.char(string='العنوان', size=100),
        'name': fields.char(string='الإسم', size=100),
        'keeper_id': fields.many2one('res.users',
                                     string='أمين المخزن', required=True),
        'product_id': fields.one2many('pro.products',
                                      'stockk_id', string='المنتجات'),
    }