#!/usr/bin/env python
# -*- coding: utf-8 -*-
import optparse
import httplib, urllib
try:
    import simplejson as json
except ImportError:
    import json
import sys
import os
import getpass

URI_DEFAULT = "ltmo.com.ar/derramo/"


class PlainHelpFormatter(optparse.IndentedHelpFormatter):
    def __init__(self,
                 indent_increment=2,
                 max_help_position=24,
                 width=None,
                 short_first=1):
        optparse.IndentedHelpFormatter.__init__ (
            self, indent_increment, max_help_position, width, short_first)

    def format_description(self, description):
        if description:
            return description + "\n"
        else:
            return ""

parser = optparse.OptionParser(
    prog='./spill.py',
    formatter=PlainHelpFormatter(),
    description=u'''
  /     \                                     
  vvvvvvv  /|__/|                             
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
   help='the message to send to the site, reads from stdin if None'
)

parser.add_option(
   '-t',
   '--tags',
   metavar='TAG,[TAG,...]', 
   type="string",
   default="",
   help='tags associated to the message'
)
parser.add_option(
   '-a',
   '--author',
   metavar='NAME', 
   type="string",
   default=getpass.getuser(),
   help='author associated to the message, not to be confused with source'
)
parser.add_option(
   '-s',
   '--source',
   metavar='NAME', 
   type="string",
   default=getpass.getuser(),
   help='source associated to the message, not to be confused with author'
)

parser.add_option(
   '-r',
   '--remote-server',
   metavar='HOST:PORT[/PATH]', 
   type="string",
   default=URI_DEFAULT,
   help='destination HOST, PORT and PATH of server, useful for debugging'
)

def get_uptime():
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
        metadata = {
            'uptime' : get_uptime()
        },
    )

    # Metadata
    print "Connecting to %s/%s ..." % (server, path)

    headers = {"Content-Type": "application/json"}
    conn = httplib.HTTPConnection(server)
    conn.request("POST","/"+path, json.dumps(values), headers)
    response = conn.getresponse()
    print response.status, response.reason
    print response.read()
    conn.close()



