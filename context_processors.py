import os

from django.conf import settings
from django.utils import simplejson as json

def about(request):
    f = open(os.path.join(settings.BASE_DIR, 'ABOUT'), 'r')
    return {
        'about':str(f.read()),
    }
