How to add a model twice to Django admin?
+++++++++++++++++++++++++++++++++++++++++++++++


You need to add the :code:`Hero` model twice to the admin, one as a regular admin area, and one as read only admin. (SOme user will potentially see only the read only admin.)

If you have try to register the same model twice::

    admin.site.register(Hero)
    admin.site.register(Hero)

you will get an error like this::

    raise AlreadyRegistered('The model %s is already registered' % model.__name__)

THe solution is to sublass the :code:`Hero` model as a ProxyModel.::

    # In models.py
    class HeroProxy(Hero):

        class Meta:
            proxy = True

    ...
    # In admin.py
    @admin.register(Hero)
    class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
        list_display = ("name", "is_immortal", "category", "origin", "is_very_benevolent")
        ....


    @admin.register(HeroProxy)
    class HeroProxyAdmin(admin.ModelAdmin):
        readonly_fields = ("name", "is_immortal", "category", "origin",
            ...)

