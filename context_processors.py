import os

from django.conf import settings
from django.utils import simplejson as json
from github2.client import Github



def about(request):
    github = Github(username=settings.GITHUB_USER, api_token=settings.GITHUB_API_TOKEN)
    f = open(os.path.join(BASE_DIR, 'README.markdown'), 'r')
    return {
        'about':str(f.read()),
        'repository':github.repos.show("tutuca/ltmo")
    }
