How to add additional actions in Django admin?
+++++++++++++++++++++++++++++++++++++++++++++++

Django admin allows you to add additional actions which allow you to do bulk actions.
You have been asked to add an action which will mark multiple :code:`Hero` s as immortal.

You can do this by adding the action as method to ModelAdmin
and adding the method as a string to :code:`actions` ::

    actions = ["mark_immortal"]

    def mark_immortal(self, request, queryset):
        queryset.update(is_immortal=True)

