#!/usr/bin/env python
# -*- coding: utf-8 -*-
import optparse
import http, urllib
import json
import sys
import os

URI_DEFAULT = "127.0.0.1:8000"

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
Ahora el hombre es una especie errante en el espacio, un vagabundo en las estrellas.''')

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
   '-a',
   '--author',
   metavar='NAME', 
   type="string",
   default="Anonymous",
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

def uptime():
   try:
       f = open( "/proc/uptime" )
       contents = f.read().split()
       f.close()
   except:
      return None

   total_seconds = float(contents[0])
   
   # Helper vars:
   MINUTE  = 60
   HOUR    = MINUTE * 60
   DAY     = HOUR * 24

   # Get the days, hours, etc:
   days    = int( total_seconds / DAY )
   hours   = int( ( total_seconds % DAY ) / HOUR )
   minutes = int( ( total_seconds % HOUR ) / MINUTE )
   seconds = int( total_seconds % MINUTE )

   string = "%d %d:%d:%d" % (days,hours,minutes,seconds)
   
   return string

if __name__ == "__main__":
    args = parser.parse_args()
    uri = args[0].uri

    if args[0].message:
        description = args[0].message
    else:
        description = "".join(sys.stdin.readlines())
    
    if args[0].tags:
        tags = args[0].tags.split(",")
    else:
        tags = ""

    values = dict(
        author = args[0].author,
        description = description,    
        tags = tags,
        metadata = {
        }
    )

    # Metadata
    uptime = uptime()
    if uptime:
        values['metadata']['uptime'] = uptime


    print( "Connecting to %s ..." % uri)

    params = urllib.urlencode(values)
    headers = {
    "Content-Type": "application/json"
    }
    conn = http.HTTPConnection(uri)
    conn.request("POST", "/derramo/", json.dumps(values), headers)
    response = conn.getresponse()

    print(response.status, response.reason)
    print("Result:\n\n")
    print(response.read())

    conn.close()



