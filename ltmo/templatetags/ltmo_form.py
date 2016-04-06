from django import template
from django.template.loader import get_template
register = template.Library()


@register.inclusion_tag('form.html')
def show_form(form):
    return {'form': form}
    
