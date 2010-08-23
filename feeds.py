from django.contrib.syndication.views import Feed
from ltmo.models import Leak

class LeakFeed(Feed):
    title = "Derrames publicados recientemente"
    link = "/"
    description = "Derrames nuevos o actualizados"
    
    def items(self):
        return Leak.objects.order_by("-created")[:5]
        
    def item_title(self, item):
        return ' '.join(item.description.split(' ')[:4])
        
    def item_description(self, item):
        return item.description    

    
