# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def get_username():
    name = 'Nobody'
    if auth.user:
        name = auth.user.first_name+'_'+auth.user.last_name[0]
    return name

def index():
    
    posts = db().select(db.tutorP.ALL)
    return dict(posts = posts)

def index3():
    
    posts = db().select(db.tutorP.ALL)
    return dict(posts = posts)


def index2():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    posts = db().select(db.tutorP.ALL)
    return dict(posts = posts)

def profile():
    author = auth.user
    userprofiles=db().select(db.profile.ALL)
    return dict(userprofiles=userprofiles, author = author)

def profiles():
    user = request.args(0)
    theProfile = db(db.profile.name == user).select().first()
    author = auth.user
    userprofiles=db().select(db.profile.ALL)
    return dict(user = theProfile, userprofiles=userprofiles, author = author)

def editprofile():
    
    userprofiles = SQLFORM(db.profile)
    if userprofiles.process().accepted:
        # Successful processing.
        session.flash = T("Thanks for editing your Profile")
        newPage = auth.user.first_name+'_'+auth.user.last_name[0]
        userName = name=auth.user.first_name+' '+auth.user.last_name[0]+'.'
        db.profile.insert(name=userName)
        redirect(URL('default', 'profile', args=newPage ))
    return dict(userprofiles = userprofiles)



def editprofile2():
    title = request.args(0) or ''
    
    userprofiles = SQLFORM.factory(
        Field('subject1', label = 'Subject 1', requires = IS_IN_SET(CATEGORY, error_message="choose a subject!"),default ="-please choose a subject-", required = True),
        Field('subject2', label = 'Subject 2 (optional)', requires = IS_IN_SET(CATEGORY), default ="-please choose a subject-", required = False),
        Field('subject3', label = 'Subject 3 (optional)', requires = IS_IN_SET(CATEGORY), default ="-please choose a subject-", required = False),
        Field('price', requires = IS_IN_SET(PRICERANGE), default = 'Alternative Exchange' ), #per hour
        Field('bio', 'text', label = 'Service Description', requires = IS_NOT_EMPTY("Please enter a description of your services.")),
        Field('picture', label = 'Profile Picture')
    )
    
    if userprofiles.process().accepted:
        newPage = auth.user.first_name+'_'+auth.user.last_name[0]
        userName = name=auth.user.first_name+' '+auth.user.last_name[0]+'.'
        db.profile.insert(name=userName, date_created=datetime.utcnow(), bio=userprofiles.vars.bio,
                        subject1=userprofiles.vars.subject1, subject2=userprofiles.vars.subject2, subject3=userprofiles.vars.subject3, price=userprofiles.vars.price, picture=userprofiles.vars.picture)
        redirect(URL('default', 'profile', args=newPage))
    

    return dict(userprofiles = userprofiles)

def tutorposts():
    user = request.args(0)
    theProfile = db(db.profile.name == user).select().first()
    author = auth.user
    #userprofiles=db().select(db.profile.college)
    posts = db().select(db.profile.ALL)
    return dict(posts = posts, author = author)


def studentposts():
    #userprofiles=db().select(db.profile.image)
    posts = db().select(db.studentP.ALL)
    return dict(posts = posts)#,userprofile = userprofile)


def addtutor():   
    title = request.args(0) or ''
    
    form = SQLFORM.factory(
        Field('subject1', label = 'Subject 1', requires = IS_IN_SET(CATEGORY, error_message="choose a subject!"),default ="-please choose a subject-", required = True),
        Field('subject2', label = 'Subject 2 (optional)', requires = IS_IN_SET(CATEGORY), default ="-please choose a subject-", required = False),
        Field('subject3', label = 'Subject 3 (optional)', requires = IS_IN_SET(CATEGORY), default ="-please choose a subject-", required = False),
        Field('price', requires = IS_IN_SET(PRICERANGE), default = 'Alternative Exchange' ), #per hour
        Field('body', 'text', label = 'Service Description', requires = IS_NOT_EMPTY("Please enter a description of your services."))
    )
    
    if form.process().accepted:
        tutName = auth.user.first_name+'_'+auth.user.last_name[0]
        formalName = auth.user.first_name+' '+auth.user.last_name[0]+'.'
        newPage = db.tutorP.insert(name=auth.user.first_name+' '+auth.user.last_name[0]+'.')
        db.profile.insert(name=tutName, nice_name=formalName, date_created=datetime.utcnow(), body=form.vars.body, 
                        subject1=form.vars.subject1, subject2=form.vars.subject2, subject3=form.vars.subject3, price=form.vars.price, picture=auth.user.picture)
        redirect(URL('default', 'index', args=auth.user.first_name+auth.user.last_name[0]))
    
    return dict(form = form)


def addstudent():   
    title = request.args(0) or ''
    
    form = SQLFORM.factory(
        Field('subject', label = 'Subject', requires = IS_IN_SET(CATEGORY, error_message="choose a subject!"), default ="-please choose a subject-", required = True),
        Field('price', requires = IS_IN_SET(PRICERANGE), default = 'Alternative Exchange' ), #per hour
        Field('body', 'text', label = 'Service Description', requires = IS_NOT_EMPTY("Please enter a description of your services."))
    )
    
    if form.process().accepted:
        tutName = auth.user.first_name+' '+auth.user.last_name[0]
     #  newPage = db.tutorP.insert(name=auth.user.first_name+' '+auth.user.last_name[0]+'.')
        db.studentP.insert(name=tutName, date_created=datetime.utcnow(), body=form.vars.body,
                        subject=form.vars.subject, price=form.vars.price)
        redirect(URL('default', 'index', args=auth.user.first_name+auth.user.last_name[0]))
    
    return dict(form = form)



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
