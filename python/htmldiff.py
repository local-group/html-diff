#!/usr/bin/env python
#coding: utf-8


import re

from lxml.html import diff

# Chinese patch
PUNCTUATION = u'\uff02\uff03\uff04\uff05\uff06\uff07\uff08\uff09\uff0a\uff0b\uff0c\uff0d\uff0f\uff1a\uff1b\uff1c\uff1d\uff1e\uff20\uff3b\uff3c\uff3d\uff3e\uff3f\uff40\uff5b\uff5c\uff5d\uff5e\uff5f\uff60\uff62\uff63\uff64\u3000\u3001\u3003\u3008\u3009\u300a\u300b\u300c\u300d\u300e\u300f\u3010\u3011\u3014\u3015\u3016\u3017\u3018\u3019\u301a\u301b\u301c\u301d\u301e\u301f\u3030\u303e\u303f\u2013\u2014\u2018\u2019\u201b\u201c\u201d\u201e\u201f\u2026\u2027\ufe4f\ufe51\ufe54\xb7\uff01\uff1f\uff61\u3002'
# diff.split_words_re = re.compile(r'[^ \t\n\r\f\v%(p)s]+(?:[ \t\n\r\f\v%(p)s]+|$)' % dict(p=PUNCTUATION), re.U)
diff.split_words_re = re.compile(r'[^\s%(p)s]+(?:[\s%(p)s]+|$)' % dict(p=PUNCTUATION), re.U)


def htmldiff(old_html, new_html):
    return diff.htmldiff(old_html, new_html)
