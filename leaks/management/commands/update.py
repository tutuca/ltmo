from django.core.management.base import BaseCommand, CommandError
from ltmo.models import Leak

class Command(BaseCommand):
    """docstring for Command"""
    def handle(self, *args, **kwargs):
        leaks = Leak.objects.all()
        for l in leaks:
            self.stderr.write("Updating %s" % l.pk)
            try:
                l.save()
            except (Exception, ) as e:
                self.stderr.write('%s' %e)
