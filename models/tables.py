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
    Field('rating'),
    Field('college'),
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
    Field('date_created', 'datetime'),
    Field('body', 'text'),
    Field('subject1'),
    Field('price'), #per hour
    Field('college'),
    Field('studentpost','boolean', writable = False, default = False),

    )

db.profile.student_status.requires = IS_IN_SET(YEAR)
db.profile.student_status.default = 'Misc'
db.profile.student_status.required = True
