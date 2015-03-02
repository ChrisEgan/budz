from datetime import datetime

CATEGORY = ['Math', 'History', 'Writing']


db.define_table('tutor',
    Field('name', 'string')
    )



db.define_table('tutoRevision',
    Field('tutor_id', 'reference tutor'),
    Field('date_created', 'datetime'),
    Field('body', 'text'),
    Field('subject'),
    Field('price'), #per hour
    Field('rating')
    )