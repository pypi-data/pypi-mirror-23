ActiveCollab Digger
===================

Django application to integrate ActiveCollab issue reporting into Django based projects.

To use:

#. ``pip install django-activecollab-digger``
#. add ``activecollab_digger`` to ``INSTALLED_APPS``
#. add ``url(r'^digger/', include('activecollab_digger.urls'))`` to ``urls.py``
#. add the settings::

    AC_BASE_URL = 'https://app.activecollab.com/COMPANY_ID/api/v1/'
    AC_TOKEN = ''
    AC_PROJECT_ID = 1
    AC_USER = 1

Notes
-----

The application needs to be behind authentication.


