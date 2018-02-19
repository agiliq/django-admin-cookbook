How to mark a field as readonly in admin?
++++++++++++++++++++++++++++++++++++++++++

UMSRA has temporarily decided to stop tracking the family trees of mythological entities. You have been asked to make the :code:`father`, :code:`mother` and :code:`spouse` fields readonly.

You can do this by::

    @admin.register(Hero)
    class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
        ...
        readonly_fields = ["father", "mother", "spouse"]

Your create form looks like this:

.. image::changeview_readonly.png
