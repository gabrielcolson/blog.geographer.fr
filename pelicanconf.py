#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

# LOCALE
# Useful for dates format
LOCALE = 'en_US.UTF-8'

# PLUGINS
PLUGINS = [
    'plugins.title-smart-break',
    'plugins.api',
    'plugins.sitemap',
    'plugins.readtime'
]

# SITE INFORMATION
AUTHOR = 'Geo'
SITENAME = 'Lucas Santoni'

# CHANGE FREQUENCY
# See sitemap plugin
CHANGE_FREQUENCIES = {
    'resume': 'yearly'
}

# DOCUMENT PRIORITIES
# See sitemap plugin
PRIORITIES = {
    'hexpresso-fic': 0.6
}

# EXCLUDE FROM SITE API
# See API plugin
API_EXCLUDE_SLUGS = [
    '404',
    'internet-error',
    'posts',
    'about'
]

# THEME
THEME = 'theme'

# MARKDOWN EXTENSIONS
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'guess_lang': False,
            'linenums': False
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {}
    },
    'output_format': 'html5'
}

# LINKS
TWITTER_HANDLE = 'geographeur'
MAIL = 'lucas.santoni@live.fr'
SITE = 'blog.geographer.fr'
SITEURL = f'https://{SITE}'
TWITTER_URL = 'https://twitter.com/' + TWITTER_HANDLE
GITHUB_URL = 'https://github.com/geospace'
MAIL_URL = 'mailto:' + MAIL

# STATIC_PATHS
STATIC_PATHS = ['assets', 'static-root']

# STATIC FILES AT ROOT
EXTRA_PATH_METADATA = {
    'static-root/levenshtein.js': {'path': 'levenshtein.js'},
    'static-root/service-worker.js': {'path': 'service-worker.js'},
    'static-root/favicon.ico': {'path': 'favicon.ico'},
    'static-root/pwa-icon.png': {'path': 'pwa-icon.png'},
    'static-root/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'static-root/manifest.json': {'path': 'manifest.json'},
    'static-root/robots.txt': {'path': 'robots.txt'},
    'static-root/keybase.txt': {'path': 'keybase.txt'}
}

# SITE INTRO
SITE_INTRO = '''
I am a computer science enthusiast. My fields of interest are cybersecurity
and software development. Please, see the <a href="/about">about page</a> or
read <a href="/resume">my resume</a> if you want to know more.
'''

# META DESCRIPTION
SITE_DESCRIPTION = '''
A blog about computer security and programming. With CTF writeups, side
projects, memos...
'''

# PATH
PATH = 'content'

# TIME
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# FEED
FEED_ALL_RSS = 'rss.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# GENERATE
PAGE_SAVE_AS = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'

# DO NOT GENERATE
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

# BLOGROLL
LINKS = ()

# SOCIAL
SOCIAL = ()

# PAGINATION
# DEFAULT_PAGINATION = 5

# RELATIVE
# RELATIVE_URLS = True


# PROJECTS
class project():
    pass


POOL_2019 = project()
POOL_2019.name = 'PoC Security Pool 2019 [French]'
POOL_2019.emoji = '🏊‍♂️'
POOL_2019.description = '''
In early 2019, I teached ~30 EPITECH students the basics of computer
security. This is the teaching material I wrote for this occasion.
<a href="/piscine-poc-2019">Browse it here.</a>
'''

THIS_BLOG = project()
THIS_BLOG.name = 'This blog'
THIS_BLOG.emoji = '📖'
THIS_BLOG.description = '''
This blog is statically generated using
<a href="https://blog.getpelican.com/">Pelican</a>, and hosted on
<a href="https://zeit.co/dashboard">Now</a>. Feel free
to <a href="https://github.com/Geospace/blog.geographer.fr">contribute</a>.
'''

SQLI_PLATFORM = project()
SQLI_PLATFORM.name = 'SQLi Platform'
SQLI_PLATFORM.emoji = '💉'
SQLI_PLATFORM.description = '''
A WEB application written in JavaScript that makes it simple to understand
and visualize SQL injections. Easy to launch via Docker.
<a href="https://github.com/Geospace/sqli-platform">Get it here.</a>
'''

# PROJECTS
PROJECTS = [
    POOL_2019,
    THIS_BLOG,
    SQLI_PLATFORM
]
