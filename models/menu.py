# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B("BrainyApe"),XML('&trade;&nbsp;'),
                  _class="brand",_href=URL('default', 'index'))
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    if auth.user:
        usersPage = auth.user.first_name+'_'+auth.user.last_name[0]
    #else:
        #usersPage = none

    # useful links to internal and external resources
        response.menu += [
            (SPAN('Tutors', _class='highlighted'), False, 'tutorposts.html', [
            (T('View Listing of Students'), False, URL('default', 'studentposts')),
            (T('Add Post to Tutor List'), False, URL('default', 'addtutor')),
            (T('Tutor Training'), False, URL('default', 'index'))]),
            (SPAN('Students', _class='highlighted'), False, 'studentposts.html', [
            (T('View Listing of Tutors'), False, URL('default', 'tutorposts')),
            (T('Add Post to Student List'), False,  URL('default', 'addstudent'))
            ]),

            (SPAN('Profile', _class='highlighted'), False, URL('default', 'profile', args=usersPage))]
    else:   
        # useful links to internal and external resources
        response.menu += [
            (SPAN('Tutors', _class='highlighted'), False, 'tutorposts.html', [
            (T('View Listing of Students'), False, URL('default', 'studentposts')),
            (T('Add Post to Tutor List'), False, URL('default', 'addtutor')),
            (T('Tutor Training'), False, URL('default', 'index'))]),
            (SPAN('Students', _class='highlighted'), False, 'studentposts.html', [
            (T('View Listing of Tutors'), False, URL('default', 'tutorposts')),
            (T('Add Post to Student List'), False,  URL('default', 'addstudent'))
            ]),

            (SPAN('Profile', _class='highlighted'), False, URL('default', 'index'))]
   
    
if DEVELOPMENT_MENU: _()

#if "auth" in locals(): auth.wikimenu()
