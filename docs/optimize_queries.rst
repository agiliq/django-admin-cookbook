How to optimize queries in Django admin?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you have a lot of calculated fields in your admin, you can be running multipel queries per object leading to your admin can becoming quite slow.
To fix this you can override the :code:`get_queryset` method on model admin to annotate the calculated fields.

Lets take the example of this `ModelAdmin` we have for `Origin`::

    @admin.register(Origin)
    class OriginAdmin(admin.ModelAdmin):
        list_display = ("name", "hero_count", "villain_count")

        def hero_count(self, obj):
            return obj.hero_set.count()

        def villain_count(self, obj):
            return obj.villain_set.count()


This add two extra queries per row in your listview page. To fix this you can override the :code:`get_queryset` to annotate the counted fields,
and then use the annotated fields in your ModelAdmin methods.

With the changes, your ModelAdmin field looks like this::


    @admin.register(Origin)
    class OriginAdmin(admin.ModelAdmin):
        list_display = ("name", "hero_count", "villain_count")

        def get_queryset(self, request):
            queryset = super().get_queryset(request)
            queryset = queryset.annotate(
                _hero_count=Count("hero", distinct=True),
                _villain_count=Count("villain", distinct=True),
            )
            return queryset

        def hero_count(self, obj):
            return obj._hero_count

        def villain_count(self, obj):
            return obj._villain_count

There are no per object extra queries. Your admin continues to look like it did before the :code:`annotate` call.

.. image:: calculated_field.png

