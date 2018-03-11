How to get Django admin urls for specific objects?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

You have a children column displaying the names of each heroes' children. You have been asked to link each children to the change page. You can do it like this.::

    @admin.register(Hero)
    class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
        ...

        def children_display(self, obj):
            display_text = ", ".join([
                "<a href={}>{}</a>".format(
                        reverse('admin:{}_{}_change'.format(obj._meta.app_label, obj._meta.model_name),
                        args=(child.pk,)),
                    child.name)
                 for child in obj.children.all()
            ])
            if display_text:
                return mark_safe(display_text)
            return "-"

The :code:`reverse('admin:{}_{}_change'.format(obj._meta.app_label, obj._meta.model_name), args=(child.pk,))`, gives the change url for an object.

The other options are

* Delete: :code:`reverse('admin:{}_{}_delete'.format(obj._meta.app_label, obj._meta.model_name), args=(child.pk,))`
* History: :code:`reverse('admin:{}_{}_history'.format(obj._meta.app_label, obj._meta.model_name), args=(child.pk,))`
