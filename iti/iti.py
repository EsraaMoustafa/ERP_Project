from openerp.osv import orm, fields


class iti_students(orm.Model):
    _name = "iti.students"

    _columns = {
        'name': fields.char('Name'),
        'age': fields.integer('age'),
        'salary': fields.float('Salary'),
        'education': fields.char('Education'),
        'faculty': fields.char('Faculty'),
        'graduation_year': fields.integer('Graduation Year'),
        'grade': fields.selection([
                                      ('g', 'Good'),
                                      ('vg', 'Very Good'),
                                      ('e', 'Excellent')], 'Grade', required=True),
        'info': fields.boolean('Accepted'),
        'signature': fields.html('Signature'),
        'department_id': fields.many2one('iti.department', 'Department', select=True),
        "skills_id": fields.many2many('iti.skills', 'rel_student_skills', 'iti_students_id', 'iti_skills_id',
                                      string='skills', select=True)

    }

    def onchangee(self, cr, uid, ids, skills_id, context=None):
        arr = []
        rcc = skills_id[0][2]
        for rc in rcc:
            record = self.pool.get('iti.department').search(cr, uid, [('skill_id', '=', rc)], context=context)
            name = record[0]
            if name not in arr:
                arr.append(name)
        if len(arr) == 1:
            v = {'department_id': arr[0]}
            return {'value': v}
        else:
            v = {'department_id': ''}
            return {'value': v}


    def onchangeee(self, cr, uid, ids, department_id, context=None):
        # record = self.pool.get('iti.skills').search(cr, uid, [('department_id', '=', department_id)], context=context)
        # return {'domain': {'skills_id': [('id', 'in', record)]}}
        # record = self.pool.get('iti.department').write(cr, uid,department_id , context=context)
        # name=record.name
        # v = {'signature': name}
        # return {'value': v}
        self.write(self, cr, uid, ids,[('name','mohamed')], context=context)


    def func1(self, cr, uid, ids, context=None):
       v = {'age': 23}
       return {'value': v}


class iti_department(orm.Model):
    _name = "iti.department"

    _columns = {
        'name': fields.char('Name'),
        'iti_students_id': fields.one2many('iti.students', 'department_id', 'Student Names', select=True),
        'skill_id': fields.one2many('iti.skills', 'department_id', 'skills', select=True),
    }


class iti_skills(orm.Model):
    _name = "iti.skills"

    _columns = {
        'name': fields.char('Name'),
        'department_id': fields.many2one('iti.department', 'skill_id', 'Department', select=True),
    }








