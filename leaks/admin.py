from django.contrib import admin
from leaks.models import Leak

class LeakAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'tags', 'author', 'created')
    list_filter = ('author', 'created')

admin.site.register(Leak, LeakAdmin)
