django-cloudflare-push
======================

About
-----

django-cloudflare-push is a simple, passwordless authentication method based on
a one-time token sent over email. There is no user registration per se, only
login. The user enters their email on the login page, and a one-time link that
is only valid for a few minutes  is generated and sent in an email. The user
clicks on the link and is immediately logged in.

[![PyPI version](https://img.shields.io/pypi/v/django-cloudflare-push.svg)](https://pypi.python.org/pypi/django-cloudflare-push)


Installing django-cloudflare-push
---------------------------------

* Install django-cloudflare-push using pip: `pip install django-cloudflare-push`

* Add tokenauth to your authentication backends:

```python
MIDDLEWARE = (
    'django_cloudflare_push.middleware.push_middleware',
    ...
)
```

Done! Your static media will be pushed. You can test the middleware by looking
for the `Link` header.


License
-------

This software is distributed under the BSD license.
