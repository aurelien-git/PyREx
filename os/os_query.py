#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Query DB
# Created on : Sun Nov 16 07:43:00 2014
#
# Write with Emacs-Nox
#
# References
#
# import sqlite3 def sys curs cursors connect
#
#
# Course material
#
# Python book - Own modification
#

#
# OS Query is made to works with an existant DB or made
# with importdb.py you can find at github.com/k0d3x
#

import sqlite3, sys

conn = sqlite3.connect('os_sys.db')
curs = conn.cursor()

query = 'SELECT * FROM faif WHERE %s' % sys.argv[1]
print query
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    print '%s: %s' % pair
    print
