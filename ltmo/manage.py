#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ltmo.settings")
    from django.core.management import execute_from_command_line
    import django
    from django.utils.encoding import smart_str
    django.utils.encoding.smart_text = smart_str

    execute_from_command_line(sys.argv)
    
if __name__ == "__main__":
    main()

