# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []

## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Mail, os, Service, PluginManager

auth = Auth(db)
crud = Crud(db)
mail = auth.settings.mailer
mail.settings.server = 'smtp.example.com:25'
mail.settings.sender = 'you@example.com'
mail.settings.login = 'username:password'

CATEGORY = ['Math', 'History', 'Writing', '-please choose a subject-']
MAJOR = ['Anthropology', 'Applied Physics','Art','Biochemistry and Molecular Biology','Bioengineering','Bioinformatics','Biology',
         'Business Management Economics','Chemistry','Classical Studies','Cognitive Science','Community Studies','Computer Engineering',
         'Computer Science','Computer Science: Computer Game Design','Critical Race and Ethnic Studies','Earth Sciences','Ecology and Evolution',
         'Economics','Education and Teaching','Electrical Engineering','Environmental Studies','Feminist Studies','Field and Exchange Programs'
         ,'Film & Digital Media','German Studies','Global Economics','History','History of Art and Visual Culture','Human Biology',
         'Italian Studies','Jewish Studies','Language Studies','Latin American and Latino Studies','Legal Studies','Linguistics','Literature'
         ,'Marine Biology','Mathematics','Molecular, Cell, and Developmental Biology','Music','Network and Digital Technology',
         'Neuroscience Physics','Physics (Astrophysics)','Physics Education','Plant Sciences','Politics','Prelaw','Premedicine','Psychology',
         'Robotics Engineering','Sociology','Spanish Studies','Technology and Information Management','The Philosophy Major','Theater Arts','Writing' ]
COLLEGES = ['College Eight', 'College Nine', 'College Ten', 'Cowell College', 
            'Crown College', 'Kresge College', 'Merrill College', 'Oakes College', 'Porter College', 'Stevenson College', 'Unaffiliated']
GENDERS = ['Male', 'Female', 'Other']
PRICERANGE = ['Alternative Exchange',1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50]
YEAR = ['Freshman', 'Sophomores', 'Junior', 'Senior', 'Grad-Student', 'Alumni']

auth.settings.extra_fields['auth_user']=[
    Field('picture', 'upload'),
    Field('name', 'string'),
    Field('nice_name', 'string'),
    Field('date_created', 'datetime'),
    Field('bio', 'text', default=''),
    Field('gender',requires = IS_IN_SET(GENDERS), default = 'Other'),
    Field('college', requires = IS_IN_SET(COLLEGES), default = 'Unaffiliated'),
    Field('student_status', requires = IS_IN_SET(YEAR, zero = '~Your level of education~'), required = False),
    Field('on_campus', 'boolean'),
    Field('major', label = 'Major', requires = IS_IN_SET(MAJOR, error_message="choose a major!"), default = "-please choose a Major-", required = False),
    Field('subject1', label = 'Subject 1', requires = IS_IN_SET(CATEGORY, error_message="choose a subject!", zero = "-please choose a subject-"), required = False),
    Field('subject2', label = 'Subject 2 (optional)', requires = IS_IN_SET(CATEGORY), default="-please choose a subject-", required = False),
    Field('subject3', label = 'Subject 3 (optional)', requires = IS_IN_SET(CATEGORY), default = "-please choose a subject-", required = False),

    Field('price', requires = IS_IN_SET(PRICERANGE), default = 'Alternative Exchange' ), #per hour
    Field('rating', writable = False),
    Field('tutorpost','boolean', writable = True, default = False)]

service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.janrain_account import use_janrain
#use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
