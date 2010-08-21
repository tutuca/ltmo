#!/usr/bin/env python
# -*- coding: utf-8 -*-
import optparse
import httplib, urllib
import simplejson
import sys
import os

URI_DEFAULT = "192.168.1.104:8000"

parser = optparse.OptionParser(
    prog='./spill.py',
    description='''\n
  /     \                           \t
  vvvvvvv  /|__/|                   \n
      I   /O,O   |
      I /_____   |      /|/|
     J|/^ ^ ^ \  |    /00  |    _//|
      |^ ^ ^ ^ |W|   |/^^\ |   /oo |
       \m___m__|_|    \m_m_|   \mm_|
''',
    epilog='''
        Las cucarachas lograron con exito su plan, echando a los pestilentes sangre caliente de sus cajas de cemento. 
Ahora el hombre es una especie errante en el espacio, un vagabundo errante en las estrellas.''')


parser.add_option(
   '-m',
   '--message', 
   metavar='TEXT',
   default=None,
   help='the message to send to the site'
)

parser.add_option(
   '-t',
   '--tags',
   metavar='TAG,[TAG,...]', 
   type="string",
   help='tags associated to the sites'
)

parser.add_option(
   '-u',
   '--uri',
   metavar='URI', 
   type="string",
   default=URI_DEFAULT,
   help='send to this URI'
)

if __name__ == "__main__":
    args = parser.parse_args()
    uri = args[0].uri

    if args[0].message:
        description = args[0].message
    else:
        description = "".join(sys.stdin.readlines())

    values = dict(
        author = "pinchila",
        description = description,    
        tags = args[0].tags.split(","),
        metadata = {}
    )

    print "Connecting to %s ..." % uri

    params = urllib.urlencode(values)
    headers = {
    "Content-Type": "application/json"}
    conn = httplib.HTTPConnection(uri)
    conn.request("POST", "/derramo/", simplejson.dumps(values), headers)
    response = conn.getresponse()

    print response.status, response.reason
    print "Result:\n\n"
    print response.read()

    conn.close()



