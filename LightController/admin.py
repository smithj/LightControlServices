from django.contrib import admin
from LightController.models import Light, Controller


# Register your models here.

class LightAdmin(admin.ModelAdmin):
    fields = ['description', 'light_id', 'controller', 'bus']
    list_display = ['description', 'light_id', 'controller', 'bus', 'on', 'color', 'brightness']

admin.site.register(Light, LightAdmin)
admin.site.register(Controller)