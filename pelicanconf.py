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
        ('Life For Music', 'http://www.lifeformusic.pl/'),
        ('RDJ.PL', 'http://rdj.pl'),
        ('Wiosenne Czarowanie', 'http://wiosenneczarowanie.info/'),
        )

# Social widget
SOCIAL = (
#          ('Facebook', 'https://www.facebook.com/ProgressiveAwake'),
          )
          
# Fresh Dance Music Social Sidebar
SOCIAL_FRESH_DANCE_MUSIC = (
    ('Facebook', 'https://www.facebook.com/FreshDanceMusicSets'),
    ('Twitter', 'https://twitter.com/freshdancemusic'),
)

# Progressive Awake Social Sidebar
SOCIAL_PROGRESSIVE_AWAKE = (
          ('Facebook', 'https://www.facebook.com/ProgressiveAwake'),
          ('Google+', 'https://plus.google.com/u/0/b/118408593215853675429/118408593215853675429/posts'),
          ('Twitter', 'https://twitter.com/progawake'),
)

# Quantum Energy Social Sidebar
SOCIAL_QUANTUM_ENERGY = (
    ('Facebook', 'https://www.facebook.com/QuantumEnergyPodcast'),
)

# Unreleased Emotions Social Sidebar
SOCIAL_UNRELEASED_EMOTIONS = (
            ('Facebook', 'https://www.facebook.com/UnreleasedEmotions'),
           )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-bootstrap3'
