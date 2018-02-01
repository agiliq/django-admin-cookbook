from django.contrib import admin


from django.contrib.auth.models import User, Group
admin.site.unregister(User)
admin.site.unregister(Group)



from django.contrib.admin import AdminSite
from .models import Epic, Event, EventHero, EventVillain


class EventAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"

event_admin_site = EventAdminSite(name='event_admin')


event_admin_site.register(Epic)
event_admin_site.register(Event)
event_admin_site.register(EventHero)
event_admin_site.register(EventVillain)
