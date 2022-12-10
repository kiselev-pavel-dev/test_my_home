from django.contrib import admin

from .models import Entity, Property


class EntityAdmin(admin.ModelAdmin):
    pass


class PropertyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Entity, EntityAdmin)
admin.site.register(Property, PropertyAdmin)
