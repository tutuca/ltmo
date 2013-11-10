#!/usr/bin/env python
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ltmo.settings")
from django.core.management import execute_from_command_line


def do_manage():
    execute_from_command_line(sys.argv)
    
if __name__ == "__main__":
    do_manage()