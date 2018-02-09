How to allow creating only one object from the admin?
=====================================================

The UMSRA admin has asked you to limit the number of categories to only one. They want every entity to be of the same category.

You can do this by::

    MAX_OBJECTS = 1

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

This would hide the add buton as soon as one object is created. You can set :code:`MAX_OBJECTS` to any value to ensure that
larger number of objects can't be ceated than :code:`MAX_OBJECTS`.
