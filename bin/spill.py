#!/usr/bin/env python
# -*- coding: utf-8 -*-
import optparse
import httplib, urllib
from subprocess import call
try:
    import simplejson as json
except ImportError:
    import json
import sys, os, signal, tempfile
import getpass

URI_DEFAULT = "ltmo.com.ar/"

def _get_editor():
    """Return a sequence of possible editor binaries for the current platform"""
    # kindly taken from bzr

    for varname in 'VISUAL', 'EDITOR':
        if varname in os.environ:
            yield os.environ[varname], '$' + varname

    if sys.platform == 'win32':
        for editor in 'wordpad.exe', 'notepad.exe':
            yield editor, None
    else:
        for editor in ['/usr/bin/editor', 'vi', 'pico', 'nano', 'joe']:
            yield editor, None
            
def _run_editor(filename):
    """Try to execute an editor to edit the commit message."""
    # kindly taken from bzr
    for candidate, candidate_source in _get_editor():
        edargs = candidate.split(' ')
        try:
            ## mutter("trying editor: %r", (edargs +[filename]))
            x = call(edargs + [filename])

        except OSError, e:
            if candidate_source is not None:
                # We tried this editor because some user configuration (an
                # environment variable or config file) said to try it.  Let
                # the user know their configuration is broken.
                trace.warning(
                    'Could not start editor "%s" (specified by %s): %s\n'
                    % (candidate, candidate_source, str(e)))
            continue
            raise

        if x == 0:
            return open(filename).read()
        elif x == 127:
            continue
        else:
            break
    print """Could not start any editor."""

def signal_handler(signal, frame):
        print '\n Cobarde!'
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

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
   default="r",
   help='tags associated to the message'
)
parser.add_option(
   '-a',
   '--author',
   metavar='NAME', 
   type="string",
   default=os.getlogin(),
   help='author associated to the message, not to be confused with source'
)
parser.add_option(
   '-s',
   '--source',
   metavar='NAME', 
   type="string",
   default='ROBADO',
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
        tempfile = tempfile.NamedTemporaryFile()
        message =  _run_editor(tempfile.name)

        if message == '' or message == '\n': 
            print('Message is blank, so is your mind, Press ^C to exit')
            description = "".join(sys.stdin.readlines()) 
        else:
            description = message

    values = dict(
        author = args[0].author,
        description = description,    
        tags =  args[0].tags,
        metadata = {
            'uptime' : get_uptime(),
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



