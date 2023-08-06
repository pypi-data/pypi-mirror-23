# Django Intlekt

A Django app for Intlekt, the content curation application using the IEML language.

## Install

Requirements:

* MongoDB **3.2** (can be installed with Docker)

```
pip install django-intlekt
```

```python
# django_project/settings.py

INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework_mongoengine',
    # These are for cross-origin requests
    # 'rest_framework.authtoken',
    # 'corsheaders',
    'django_intlekt',
]

from mongoengine import connect
connect(...)  # See http://docs.mongoengine.org/guide/connecting.html
```

```python
# django_project/urls.py

from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('django_intlekt.urls')),  # TODO: customize the route
    # ...
]
```
