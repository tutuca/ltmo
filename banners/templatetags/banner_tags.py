from django import template
from banners.models import Banner
from random import choice
register = template.Library()


@register.inclusion_tag('single.html')
def pop_slot(slot):
    banner = None
    banners = Banner.objects.filter(slot=slot)
    if banners:
        banner = choice(banners)
    return {'banner': banner}


@register.inclusion_tag('slot.html')
def lookup_banners(slot):
    try:
        banners = Banner.objects.filter(slot__icontains=slot)
    except Banner.DoesNotExists:
        banners = None
    return {'banners': banners}
