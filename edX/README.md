edX Project
===
This edX Project currently has one app (db)

To run the 'project/server'. You will require a few django modules, these can be installed by using the following commands:
pip install django-debugtools
pip install django-debug-toolbar
pip install South

In this directory run: python manage.py runserver
and try navigating with your browser to http://127.0.0.1:8000/db/base

At http://127.0.0.1:8000/admin you will find the django built-in admin panel. Our current test admin has the following credentials:
Username: admin
Password: admin
