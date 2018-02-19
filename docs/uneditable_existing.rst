How to make a field editable while creating, but read only in existing objects?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

YOu need to make the :code:`name` and :code:`category` read only once a :code:`Hero` is created. However duing the first write the fields needs to be editable.

You can do this by overriding :code:`get_readonly_fields` method, like this::

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["name", "category"]
        else:
            return []

:code:`obj` is None during the object creation, but set to the object being edited during an edit.
