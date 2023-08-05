ActiveCollab Digger
===================

Django application to integrate ActiveCollab issue reporting into Django based projects.

To use:

#. ``pip install django-activecollab-digger``
#. add ``activecollab_digger`` to ``INSTALLED_APPS``
#. add ``url(r'^digger/', include('activecollab_digger.urls'))`` to ``urls.py``
#. add the settings::

    # ActiveCollab API URL
    AC_BASE_URL = 'https://app.activecollab.com/COMPANY_ID/api/v1/'
    # ActiveCollab API token
    AC_TOKEN = ''
    # ActiveCollab project ID
    AC_PROJECT_ID = 1
    # ActiveCollab user ID to create the issues
    AC_USER = 1

Notes
-----

The application needs to be behind authentication.
