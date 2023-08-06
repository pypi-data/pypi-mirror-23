============
codebehind
============

.. image:: https://travis-ci.org/michaelhenry/codebehind.svg?branch=master
    :target: https://travis-ci.org/michaelhenry/codebehind
    
.. image:: https://img.shields.io/pypi/v/codebehind.svg
    :target: https://pypi.python.org/pypi/codebehind

.. image:: https://img.shields.io/badge/contact-@michaelhenry119-blue.svg?style=flat
    :target: https://twitter.com/michaelhenry119
    
Because i dont want to do the same thing all over again. If you are using Django Rest Framework, then this will might help you.


Features
----------

- Registration and Login
- Different Authentication Logic (Basic , Token, HMAC Signature)
- Basic Helpers
- Since it use DRF, Browsable Rest API!



Quick start
-----------

1. Add "codebehind" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'codebehind',
        'rest_framework',
    ]

2. Run `python manage.py migrate` to create the useful models.

3. In your `*settings.py`::

    REST_FRAMEWORK = {
    	# Use Django's standard `django.contrib.auth` permissions,
    	# or allow read-only access for unauthenticated users.
    	'DEFAULT_PERMISSION_CLASSES': (
    		'rest_framework.permissions.IsAdminUser',
    		'rest_framework.permissions.IsAuthenticated',
    	),
    
    	'DEFAULT_AUTHENTICATION_CLASSES': (
    	   'codebehind.authentication.CodeBehindAuthentication',
    	   'rest_framework.authentication.BasicAuthentication',
    	   'rest_framework.authentication.SessionAuthentication',
    	),
    
    	'PAGE_SIZE': 20
    }


4. in `urls.py`::

    from rest_framework import routers
    from django.conf.urls import include, url
    from codebehind.views import UsersViewSet, GroupViewSet
    
    router = routers.DefaultRouter()
    router.register(r'users', UsersViewSet,'users')
    router.register(r'groups', GroupViewSet,'groups')
    
    urlpatterns += [
        # add this
        url(r'^v1/', include(router.urls)),
    ]
    
