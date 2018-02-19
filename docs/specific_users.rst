How to restrict Django admin to specific users?
================================================

Django admin allows access to users marked as :code:`is_staff=True`.
To disable a user from being able to access the admin, you should set :code:`is_staff=True`.

This holds true even if the user is a superuser. :code:`is_superuser=True`. If a non-staff tries to access the admin, they see a message like this.

