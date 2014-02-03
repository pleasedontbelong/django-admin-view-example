Django Base project
====================

Based on http://www.jeffknupp.com/blog/2012/02/09/starting-a-django-project-the-right-way/ 
but including a base requirements file and changing the apps structure

Installing the base project
============================

- Clone repository
- Create virtualenv
- Launch `pip install -r requirements/development.txt`
- Rename `django_boot` folder with the name of the site
- Rename all instances of `django_boot` in the base.py file with the same name as before
- Create a DB and create the `local.py` files in settings (use the default template)
- Launch `python manage.py syncdb`
- Launch `python manage.py schemamigration base --initial`
- Have fun!
