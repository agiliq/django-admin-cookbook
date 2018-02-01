from django.contrib import admin

from .models import Epic, Event, EventHero, EventVillain


admin.site.register(Epic)
admin.site.register(Event)
admin.site.register(EventHero)
admin.site.register(EventVillain)
