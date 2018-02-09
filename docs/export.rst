How to export CSV from Django admin?
++++++++++++++++++++++++++++++++++++

You have been asked to add ability to export :code:`Hero` and :code:`Villain` from the admin.
There are a number of third party apps which allow doing this, but its quite easy without adding another dependency.
You will add an admin action to :code:`HeroAdmin` and :code:`VillanAdmin`.

An admin action always has this signature `def admin_action(modeladmin, request, queryset):`, alternatively you can add directly as a method on the :code:`ModelAdmin` like this::

    class SomeModelAdmin(admin.ModelAdmin):

        def admin_action(self, request, queryset):


To add csv export to :code:`HeroAdmin` you can do something like this::

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        pass

    export_as_csv.short_description = "Export Selected"

This adds an action called export selected, which looks like this

.. image:: export_selected.png

You will then change the :code:`export_as_csv` to this::

    import csv
    from django.http import HttpResponse
    ...

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

This exports all the selected rows. If you notice, :code:`export_as_csv` doens't have anything specific to :code:`Hero`,
so you can extract the method to a mixin.

With the changes, your code looks like this::


    class ExportCsvMixin:
        def export_as_csv(self, request, queryset):

            meta = self.model._meta
            field_names = [field.name for field in meta.fields]

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
            writer = csv.writer(response)

            writer.writerow(field_names)
            for obj in queryset:
                row = writer.writerow([getattr(obj, field) for field in field_names])

            return response

        export_as_csv.short_description = "Export Selected"


    @admin.register(Hero)
    class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
        list_display = ("name", "is_immortal", "category", "origin", "is_very_benevolent")
        list_filter = ("is_immortal", "category", "origin", IsVeryBenevolentFilter)
        actions = ["export_as_csv"]

    ...


    @admin.register(Villain)
    class VillainAdmin(admin.ModelAdmin, ExportCsvMixin):
        list_display = ("name", "category", "origin")
        actions = ["export_as_csv"]

You can add such export to other models by subclassing from :code:`ExportCsvMixin`
