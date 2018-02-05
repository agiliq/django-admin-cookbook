Django Admin Cookbook
===========================================================

Django Admin Cookbook - How to do things with Django admin.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This is a book about doing things with Django admin. It takes the form of about forty questions and common tasks with Django admin we answer.

The the chapters are based on a common set of models, which you can read in detail here (:doc:`models`). In short, we have two apps,
:code:`events` and :code:`entities`. The models are

* Events: :code:`Epic`, :code:`Event`, :code:`EventHero`, :code:`EventVillian`
* Entities: :code:`Category`, :code:`Origin`, :code:`Hero`, :code:`Villain`


Text and Design
+++++++++++++++++++++

.. toctree::
   :maxdepth: 1

   change_text
   plural_text
   two_admin
   remove_default
   logo
   override_default_templates
   set_ordering

Calculated fields
+++++++++++++++++++++

.. toctree::
   :maxdepth: 1

   calculated_fields
   many_to_many
   sorting_calculated_fields
   filtering_calculated_fields

Permissions
+++++++++++++++++++++

.. toctree::
   :maxdepth: 1

   specific_users
   restrict
   restrict_parts
   only_one
   remove_add_delete

Multiple models and inlines
++++++++++++++++++++++++++++++++++++++++++

.. toctree::
   :maxdepth: 1

   edit_multiple_models
   one_to_one_inline
   nested_inlines
   single_admin_multiple_models

Bulk and custom actions
++++++++++++++++++++++++++++++++++++++++++

.. toctree::
   :maxdepth: 1

   export
   import
   remove_delete_selected
   add_actions
   action_buttons

Listview Page
++++++++++++++++++++++++++++++++++++++++++

.. toctree::
   :maxdepth: 1

   increase_row_count
   disable_pagination
   date_based_filtering
   boolean_fields


Misc
++++++++++++++++++++++++++++++++++++++++++

.. toctree::
   :maxdepth: 1

   object_url
   add_model_twice
   override_save
   database_view
   optimize_queries
   set_ordering


Indices and tables
+++++++++++++++++++++
.. toctree::
   :maxdepth: 1

   models

* :ref:`genindex`
* :ref:`modindex`
