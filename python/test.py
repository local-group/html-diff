#!/usr/bin/env python
#coding: utf-8

import sys

from htmldiff import htmldiff

sys.stdout.write(htmldiff(sys.argv[1], sys.argv[2]))
