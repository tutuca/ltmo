# -*- coding: utf-8 -*-
from markdown import markdown
from django.template.defaultfilters import striptags, slugify
from ltmo.models import Leak


a = Leak.objects.all()

def reload_ltmo():
    for x in a:
         x.rendered = markdown(x.description)
         x.title = striptags(x.rendered)[:70] or u'sin título'
         x.save()
    
