# -*- coding: utf-8 -*-
# try something like

def display_form():
    form = SQLFORM(db.blog)
    if form.process().accepted:
        session.flash = 'form accepted'
        redirect(URL('thanks'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'plase fill out the form'
    return locals()

def thanks():
    msg = "Thank you for submitting your post"
    return locals()

def update():
    record = db.blog(request.args(0)) or redirect(URL('post'))
    form = SQLFORM(db.blog, record)
    if form.process().accepted:
        response.flash = T('Record Updated')
    else:
        response.flash = T('Please complete the form.')
    return locals()

def index(): return dict(message="hello from blog.py")

def post():
    form = SQLFORM(db.blog).process()
    return locals()

def view():
    rows = db(db.blog).select(orderby=~db.blog.id)
    return locals()