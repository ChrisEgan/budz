from datetime import datetime

def get_username():
    name = 'Nobody'
    if auth.user:
        name = auth.user.first_name+'_'+auth.user.last_name[0]
    return name
CATEGORY = ['Math', 'History', 'Writing', '-please choose a subject-']
MAJOR = ['Math', 'History', 'Writing', '-please choose a major-']
COLLEGES = ['College Eight', 'College Nine', 'College Ten', 'Cowell College', 
            'Crown College', 'Kresge College', 'Merrill College', 'Oakes College', 'Porter College', 'Stevenson College', 'Unaffiliated']
GENDERS = ['Male', 'Female', 'Other']
PRICERANGE = ['Alternative Exchange',1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50]
YEAR = ['Freshman', 'Sophomores', 'Junior', 'Senior', 'Grad-Student', 'Alumni']


db.define_table('profile',
    Field('name', 'string'),
    Field('nice_name', 'string'),
    Field('date_created', 'datetime'),
    Field('email'),
    Field('bio', 'text'),
    Field('bio2', 'text'),
    Field('body', 'text'),
    Field('college'),
    Field('student_status'),
    Field('picture', 'upload'),
    Field('subject1'),
    Field('subject2'),
    Field('subject3'),
    Field('major'),
    Field('price'), #per hour
    Field('tutorpost','boolean', writable = False, default = False),
    Field('studentpost','boolean', writable = False, default = False)
    )

db.define_table('tutorP',
    Field('name', 'string'),
    Field('date_created', 'datetime'),
    Field('body', 'text'),
    Field('subject1'),
    Field('subject2'),
    Field('subject3'),
    Field('price'), #per hour
    Field('rating'),
    Field('college'),
    Field('tutorpost','boolean', writable = False, default = False),
    )

db.define_table('studentP',
    Field('name', 'string'),
    Field('nice_name', 'string'),
    Field('date_created', 'datetime'),
    Field('email'),
    Field('body', 'text'),
    Field('college'),
    Field('student_status'),
    Field('picture', 'upload'),
    Field('subject'),
    Field('major'),
    Field('price_min'),
    Field('price_max'),

    )

db.profile.student_status.requires = IS_IN_SET(YEAR)
db.profile.student_status.default = 'Misc'
db.profile.student_status.required = True

#borrowed a search implementation: http://www.web2pyslices.com/slice/show/1403/dynamic-search
def build_query(field, op, value):
    if op == 'equals':
        return field == value
    elif op == 'not equal':
        return field != value
    elif op == 'greater than':
        return field > value
    elif op == 'less than':
        return field < value
    elif op == 'starts with':
        return field.like(value+'%')
    elif op == 'ends with':
        return field.like('%'+value)
    elif op == 'contains':
        return field.like('%'+value+'%')

def dynamic_search(table, *params):
    tbl = TABLE()
    selected = []
    ops = [opers]
    query = table.id > 0    
    for field in table.fields:
        for param in params:
            if field == param:
                chkval = request.vars.get('chk'+field,None)
                txtval = request.vars.get('txt'+field,None)
                opval = request.vars.get('op'+field,None)
                row = TR(TD(INPUT(_type="checkbox",_name="chk"+field,
                                  value=chkval=='on')),
                         TD(field),TD(SELECT(ops,_name="op"+field,
                                             value=opval)),
                         TD(INPUT(_type="text",_name="txt"+field,
                                  _value=txtval)))
                tbl.append(row)
                if chkval:
                    if txtval:
                        query &= build_query(table[field], 
                                        opval,txtval)
            selected.append(table[field])           
    form = FORM(tbl,INPUT(_type="submit"))
    results = db(query).select(*selected)
    return form, results