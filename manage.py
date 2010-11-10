#!/usr/bin/env python

from django.core.management import execute_manager
from ltmo import settings

def manage():
    return execute_manager(settings)
    
if __name__ == '__main__':
    manage()
