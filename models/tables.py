from datetime import datetime

def get_username():
    name = 'Nobody'
    if auth.user:
        name = auth.user.first_name+'_'+auth.user.last_name[0]
    return name

CATEGORY = ['Math', 'History', 'Writing', '-please choose a subject-']
YEAR = ['Freshman', 'Sophomores', 'Junior', 'Senior', 'Grad-Student', 'Alumni']

db.define_table('profile',
    Field('name', 'string'),
    Field('date_created', 'datetime'),
    Field('email'),
    Field('bio', 'text'),
    Field('college'),
    Field('student_status'),
    Field('picture', 'upload'),
    Field('subject1'),
    Field('subject2'),
    Field('subject3'),
    Field('price'), #per hour
    Field('rating')
    )

db.define_table('tutorP',
    Field('name', 'string'),
    Field('date_created', 'datetime'),
    Field('body', 'text'),
    Field('subject1'),
    Field('subject2'),
    Field('subject3'),
    Field('price'), #per hour
    Field('rating')
    )

db.define_table('studentP',
    Field('name', 'string'),
    Field('date_created', 'datetime'),
    Field('body', 'text'),
    Field('subject'),
    Field('price'), #per hour
    )

db.profile.student_status.requires = IS_IN_SET(YEAR)
db.profile.student_status.default = 'Misc'
db.profile.student_status.required = True
