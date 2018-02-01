from django.contrib import admin

from .models import Epic, Event, EventHero, EventVillain
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Epic)
admin.site.register(Event)
admin.site.register(EventHero)
admin.site.register(EventVillain)
