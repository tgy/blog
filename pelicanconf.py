#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Valentin Iovene'
SITENAME = 'Valentin Iovene (a.k.a. toogy/tgy)'
SITEURL = 'https://blog.too.gy'

# Content with dates in the future will get a default status of 'draft'
WITH_FUTURE_DATES = False

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),)

LINKS = (('about', 'https://too.gy'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'theme'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    # 'render_math',
    'pandoc_reader',
]

STATIC_PATHS = ['assets']

for file in os.listdir(os.path.join(PATH, 'posts')):
    if os.path.isdir(os.path.join(PATH, 'posts', file)):
        STATIC_PATHS.append(os.path.join('posts', file))

ARTICLE_PATHS = ['posts']

PANDOC_ARGS = [
    '--mathjax',
    '--smart',
    # '--number-sections',
    '--highlight-style', 'pygments',
]

PANDOC_EXTENSIONS = [
    # '+hard_line_breaks',
]

# MATH_JAX = {
    # 'force_tls': True,
# }
