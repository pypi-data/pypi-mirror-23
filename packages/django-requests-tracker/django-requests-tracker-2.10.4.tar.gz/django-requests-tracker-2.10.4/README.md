# django-requests-tracker

Tracking http requests send by [python-requests](https://github.com/kennethreitz/requests) inside a [Django](https://www.djangoproject.com) application.

## Installation

To install using `pip`:

```bash
$ pip install django-requests-tracker
```

To install using `easy_install`:

```bash
$ easy_install django-requests-tracker
```

## Configuration

Put `requests_tracker` into your `INSTALLED_APPS`:

```python
    INSTALLED_APPS = [
        ...
        'requests_tracker',
    ]
```

Then create `requests_tracker` database tables by running:

```bash
$ python manage.py migrate
```
