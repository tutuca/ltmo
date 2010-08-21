#!/usr/bin/env python
# -*- coding: utf-8 -*-
import optparse
import httplib, urllib
import simplejson
import sys
import os
import getpass

URI_DEFAULT = "127.0.0.1:8000/derramo"

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
   default="",
   help='tags associated to the sites'
)

parser.add_option(
   '-a',
   '--author',
   metavar='NAME', 
   type="string",
   default=getpass.getuser(),
   help='tags associated to the sites'
)

parser.add_option(
   '-r',
   '--remote-server',
   metavar='HOST:PORT[/PATH]', 
   type="string",
   default=URI_DEFAULT,
   help='destination HOST, PORT and PATH of server'
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

   string = "%d %s, %d:%d:%d" % (days,
            days > 1 and 'days' or 'day', hours, minutes, seconds)
   
   return string

if __name__ == "__main__":
    args = parser.parse_args()

    remote = args[0].remote_server.split("/")
    server = remote[0]
    if len(remote) > 1: 
        path = "/".join(remote[1:])
    else:
        path = ""
            
    if args[0].message:
        description = args[0].message
    else:
        description = "".join(sys.stdin.readlines())

    values = dict(
        author = args[0].author,
        description = description,    
        tags =  args[0].tags,
        metadata = {},
    )

    # Metadata
    uptime = uptime()
    if uptime:
        values['metadata']['uptime'] = uptime

    print "Connecting to %s/%s ..." % (server, path)

    headers = {"Content-Type": "application/json"}
    conn = httplib.HTTPConnection(server)
    conn.request("POST","/"+path, simplejson.dumps(values), headers)
    response = conn.getresponse()

    print response.status, response.reason
    print "Result:\n\n"
    print response.read()

    conn.close()



