# -*- coding: utf-8 -*-
from __future__ import unicode_literals


__version__ = '0.7.5'

DEFAULT_BASEIMAGE = 'tianon/true:latest'
DEFAULT_COREIMAGE = 'busybox:latest'
DEFAULT_HOSTNAME_REPLACEMENT = [
    ('_', '-'),
    ('.', '-'),
]
