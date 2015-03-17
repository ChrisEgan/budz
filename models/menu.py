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
    else:
        usersPage = ''

    # useful links to internal and external resources
    response.menu += [
        (SPAN('For Tutors', _class='highlighted'), False, URL('default', 'tutorposts'), [
        (T('Find a Pupil'), False, URL('default', 'studentposts')),
        (T('Become a tutor! (Upgrade your Profile)'), False, URL('default', 'profile', args=usersPage)),
        (T('How to be a Tutor'), False, URL('default', 'tutorhelper'))]),
        (SPAN('For Students', _class='highlighted'), False, URL('default', 'studentposts'), [
        (T('Find a Tutor'), False, URL('default', 'tutorposts')),
        (T('Request a Tutor'), False,  URL('default', 'addstudent'))    
        ]),

        (SPAN('Profile', _class='highlighted'), False, URL('default', 'profile', args=usersPage))]
    
   
    
if DEVELOPMENT_MENU: _()

#if "auth" in locals(): auth.wikimenu()
