from django import template
import urllib, hashlib

register = template.Library()

@register.simple_tag
def gravatar(email, size=50, rating='g', default=None):
    """
    Returns a gravatar url. It's well documented because it's stollen.
    I don't remember which djangosnippet I take this from.

    Example tag usage: {% avatar user.email 80 "g" %}

    :Parameters:
       - `email`: the email to send to gravatar.
       - `size`: optional YxY size for the image.
       - `rating`: optional rating (g, pg, r, or x) of the image.
       - `default`: optional default image url or hosted image like wavatar.
    """
    # Verify the rating actually is a rating accepted by gravatar
    rating = rating.lower()
    ratings = ['g', 'pg', 'r', 'x']
    if rating not in ratings:
        raise template.TemplateSyntaxError('rating must be %s' % (
            ", ".join(ratings)))
    # Create and return the url
    hash = hashlib.md5(email).hexdigest()
    url = 'http://www.gravatar.com/avatar/%s?s=%s&r=%s' % (
        hash, size, rating)
    
    return """<img src="%s" width="%s" height="%s" alt="avatar" class="gravatar" />""" % (url, size, size)

