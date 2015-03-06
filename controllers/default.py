# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    posts = db().select(db.tutorP.ALL)
    return dict(posts = posts)
    
    

def add():   
    title = request.args(0) or ''
    
    form = SQLFORM.factory(
        Field('subject1', label = 'Subject 1', requires = IS_IN_SET(CATEGORY, error_message="choose a subject!"),default ="-please choose a subject-", required = True),
        Field('subject2', label = 'Subject 2 (optional)', requires = IS_IN_SET(CATEGORY), default ="-please choose a subject-", required = False),
        Field('subject3', label = 'Subject 3 (optional)', requires = IS_IN_SET(CATEGORY), default ="-please choose a subject-", required = False),
        Field('price', requires = IS_FLOAT_IN_RANGE(0, 100.00, error_message='The price should be in the range 0..100')),
        Field('body', 'text', label = 'Service Description', requires = IS_NOT_EMPTY("Please enter a description of your services."))
    )
    
    if form.process().accepted:
        tutName = auth.user.first_name+'_'+auth.user.last_name[0]
        newPage = db.tutorP.insert(name=auth.user.first_name+' '+auth.user.last_name[0]+'.')
        db.tutorP.insert(name=tutName, date_created=datetime.utcnow(), body=form.vars.body, 
                        subject1=form.vars.subject1, subject2=form.vars.subject2, subject3=form.vars.subject3, price=form.vars.price)
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
