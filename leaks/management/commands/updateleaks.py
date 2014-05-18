from django.core.management.base import BaseCommand
from ltmo.models import Leak

class Command(BaseCommand):
    help = 'Updates leaks saving every leak available.'

    def handle(self, *args, **options):
        for leak in Leak.objects.all():

            try:
                leak.save()
            except Exception as e:
                self.stdout.write(e.message+'\n')
            else:
                self.stdout.write('Saving leak %s \n' %leak.id)