from django.contrib.syndication.views import Feed
from ltmo.models import Leak

class LeakFeed(Feed):
    title = "Derrames publicados recientemente"
    link = "/"
    description = "Derrames nuevos o actualizados"
    description_template = 'feeds/description.html'

    def items(self):
        return Leak.objects.order_by("-created")[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
