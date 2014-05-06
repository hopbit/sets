#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'\u0141ukasz Siwi\u0144ski'
SITENAME = u'DJ Sets'
SITEURL = 'http://siwinski.info/sets'

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
        ('Einar Mixes','http://einarmixes.blogspot.com/'),
        ('GeeCON','http://geecon.org'),
        ('Life For Music', 'http://www.lifeformusic.pl/'),
        ('Mobile Warsaw', 'http://mobile-warsaw.pl'),
        ('RDJ.PL', 'http://rdj.pl'),
        ('Vigeo Games', 'http://blog.vigeogam.es/'),
        ('Warsjawa', 'http://warsjawa.pl'),
        ('WJUG', 'http://www.warszawa.jug.pl/'),
        )

# Social widget
SOCIAL = (
          ('Facebook', 'https://www.facebook.com/ProgressiveAwake'),
          ('Facebook', 'https://www.facebook.com/QuantumEnergyPodcast'),
          ('BitBucket', 'https://bitbucket.org/hopbit'),
          ('GitHub', 'https://github.com/hopbit'),
          ('Google+', 'https://plus.google.com/113990170437825708147/posts'),
          ('Twitter', 'https://twitter.com/lsiwinski'),
          ('YouTube', 'http://www.youtube.com/user/yhopbit'),
          ('GoldenLine', 'http://www.goldenline.pl/lukasz-siwinski/'),
          ('Gravatar', 'http://pl.gravatar.com/hopbit'),
          ('Lasf.fm', 'http://www.lastfm.pl/user/lsiwinski'),
          ('StackOverflow', 'http://stackoverflow.com/users/235973/lukasz-siwinski'),
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-bootstrap3'
