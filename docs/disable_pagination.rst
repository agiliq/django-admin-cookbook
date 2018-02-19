How to disable django admin pagination?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you want to completely disable pagination on a admin listview page, you can do this. ::


    import sys
    ...

    @admin.register(Hero)
    class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
        ...

        list_per_page = sys.maxsize

You can also read :doc:`increase_row_count`.
