# Django Intlekt

A Django app for Intlekt, the content curation application using the IEML language.

## Install

Requirements:

* MongoDB **3.2** (can be installed with Docker)

```
git clone https://github.com/IEMLdev/django-intlekt
cd django-intlekt
python setup.py install
```

```python
# django_project/settings.py

INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework_mongoengine',
    # 'rest_framework.authtoken',
    # 'corsheaders',
    'django_intlekt',
]

from mongoengine import connect
connect(...)
```
