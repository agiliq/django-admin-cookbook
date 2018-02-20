How to override save behaviour for Django admin?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

:code:`ModelAdmin` has a :code:`save_model` method, which is used for creating and updating model objects.
By overriding this, you can customize the save behaviour for admin.


The :code:`Hero` model has the following field.::

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
            null=True, blank=True, on_delete=models.SET_NULL)


If you want to always save the current user whenever the Hero is updated, you can do.::

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)


