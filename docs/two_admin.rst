How to create two independent admin sites?
===========================================================

The usual way to create admin pages is to put all models in a single admin. However it is possible to have multiple admin sites in a single Django app.

Right now our :code:`entity` and :code:`event` models are in same place. UMSRA has two distinct group researching `Events` and `Entities`, and so  wants to split the admins.


We will keep the default admin for `entities` and create a new subclass of :code:`AdminSite` for `events`.

In our :code:`events/admin.py` we do::

    class EventAdminSite(AdminSite):
        site_header = "UMSRA Events Admin"
        site_title = "UMSRA Events Admin Portal"
        index_title = "Welcome to UMSRA Researcher Events Portal"

    event_admin_site = EventAdminSite(name='event_admin')


    event_admin_site.register(Epic)
    event_admin_site.register(Event)
    event_admin_site.register(EventHero)
    event_admin_site.register(EventVillain)

And change the :code:`urls.py` to ::

    from events.admin import event_admin_site


    urlpatterns = [
        path('entity-admin/', admin.site.urls),
        path('event-admin/', event_admin_site.urls),
    ]


This separates the admin. Noth admins are available at their respective urls, :code:`/entity-admin/` and :code:`event-admin/`.
