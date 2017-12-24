#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mukesh kumar Gupta'
SITENAME = u"Mukesh's blog"
SITEURL = ''
SITETITLE  = AUTHOR
SITESUBTITLE = 'Software Engineer'
SITELOGO='https://en.gravatar.com/userimage/12923662/b0ee456698191dc86b477844aef2a0da.jpg?130'
THEME = '/usr/blog'
THEME = '/usr/blog'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True


LINKS = (('About','#'), 
         ('Portfolio', '#'))
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017
# Social widget
SOCIAL = (('linkedin','https://linkedin.com/in/mkshkmrgpt'),
          ('github', 'https://github.com/mkshkmrgpt'),
          ('google','https://google.com/+mkshkmrgpt'),
          ('facebook','https://facebook.com/mkshkmrgpt'))

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
