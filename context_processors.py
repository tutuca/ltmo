import os
from urllib2 import urlopen

from django.conf import settings
from django.utils import simplejson as json



def about(request):
    
    f = open('README.markdown', 'r')
    github_json = urlopen('http://github.com/api/v2/json/repos/show/tutuca/ltmo')
    repository = json.loads(github_json.read())
    import ipdb; ipdb.set_trace()    
    return {
        'about':str(f.read()),
        'repository':repository
    }
