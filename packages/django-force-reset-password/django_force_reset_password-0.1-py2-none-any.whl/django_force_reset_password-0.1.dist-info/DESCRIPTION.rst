=====
Django force reset password
=====

This is an application to make every users to reset their password(only admin users)

Quick start
-----------

1. Add "django_force_reset_password" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_force_reset_password',
    ]

2. Include the django_force_reset_password URLconf in your project urls.py like this::


    from django_force_reset_password.views import pfr_password_change, pfr_login


    urlpatterns = [
        ......
        url(r'^admin/login/$', pfr_login),
        url(r'^admin/password_change/$', pfr_password_change),
        url(r'^admin/', admin.site.urls),
        ....
    ]


4. add 'django_force_reset_password.middleware.FPRCheck' in MIDDLEWARE_CLASSES settings like this

    MIDDLEWARE_CLASSES = [
        ....

        'django_force_reset_password.middleware.FPRCheck'
        ]



