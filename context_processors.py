from django.conf import settings
import os
def about(request):

    f = open('README.markdown', 'r')
    return {'about':str(f.read())}
