from django.contrib import admin

# Register your models here.

from .models import *

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_link', 'last_updated', 'created')

admin.site.register(Module, ModuleAdmin)
admin.site.register(Course)
admin.site.register(Task)