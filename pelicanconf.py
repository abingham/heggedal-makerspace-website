#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os

AUTHOR = 'Austin Bingham'
SITENAME = 'Make Heggedal'
SITEURL = ''
THEME = 'themes/maker'

PATH = 'content'

TIMEZONE = 'Europe/Oslo'

DEFAULT_LANG = 'no'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = [os.environ['PELICAN_PLUGIN_DIR']]
PLUGINS = ['i18n_subsites']

I18N_SUBSITES = {
    'no': {
        'SITENAME': 'Make Heggedal',
    },
    'en': {
        'SITENAME': 'Make Heggedal',
    }
}

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}
I18N_GETTEXT_LOCALEDIR = 'themes/maker/translations'
I18N_GETTEXT_DOMAIN = 'messages'