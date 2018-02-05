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
   :caption: Contents:


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
   :caption: Contents:

   calculated_fields
   many_to_many
   sorting_calculated_fields
   filtering_calculated_fields


Indices and tables
+++++++++++++++++++++
.. toctree::
   :maxdepth: 1

   models

* :ref:`genindex`
* :ref:`modindex`
