How to associate model with current user while saving?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The :code:`Hero` model has the following field.::

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
            null=True, blank=True, on_delete=models.SET_NULL)


You want the :code:`added_by` field to be automatically set to current user whenever object is created from admin. You can do this.::

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.added_by = request.user
        super().save_model(request, obj, form, change)

If instead you wanted to always save the current user, you can do.::

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)

If you also want to hide the :code:`added_by` field to not show up on the change form, you can do.::


    @admin.register(Hero)
    class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
        ...
        exclude = ['added_by',]

