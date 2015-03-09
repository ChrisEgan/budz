from datetime import datetime

CATEGORY = ['Math', 'History', 'Writing', '-please choose a subject-']

db.define_table('profile',
    Field('name', 'string'),
    Field('date_created', 'datetime'),
    Field('email'),
    Field('bio', 'text'),
    Field('college'),
    Field('professor'),
    #Field('picture', 'upload'),
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
