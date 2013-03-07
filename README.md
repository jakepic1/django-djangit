django-djangit
==============

Django app for git integration and database management.

djangit's primary feature is its ability to make branch-local copies of a database for each git branch, and dynamically switch between the different databases.

For example, if you create a database called ``proj_db``, and and create a new branch called ``feature`` with djangit,
djangit will create and use a database called ``proj_db_feature``.

This is useful when you want to keep the data or schema different in separate branches, particularly when combined with south for schema/data migrations.


Installation
------------
In your settings file, include ``djangit`` in your INSTALLED_APPS.

By default, djangit will append the current branch name to each database in your django settings module. To ignore certain branches, use the settings variable ``DJANGIT_IGNORE_BRANCHES``:

```python
DJANGIT_IGNORE_BRANCHES = (
    'master',
)
```

Then, to enable djangit's database switching, include the following at the bottom of the settings file (after the ``DATABASES`` setting is defined):

```python
# Include djangit database snippet.
from djangit.settings import setup_dbs, copy_original_dbs
DATABASES_ORIGINAL = copy_original_dbs(DATABASES)
setup_dbs(DATABASES, DJANGIT_IGNORE_BRANCHES)
```

Create a new branch
--------------------
This will create a branch called ``test``, copy the current  databases to ``dbname_test``, and push the new branch to the origin repo.

```
./manage.py branch create test --origin
```

Create a branch ``test`` without copying the database and without pushing to origin.

```
./manage.py branch create test --no-db
```

Delete a branch
------------------
Delete branch test and its databases, including in origin.

```
./manage.py branch delete test --origin
```

Checkout a branch
-----------------
Checkout branch from origin, and create its databases.

```
./manage.py branch checkout test --origin
```

Copy databases
-----------------
Copy the current databases in the DATABASES setting, with a suffix of ``_test`` for all their names.

```
./manage copydb test
```

Drop databases
----------------
Drop databases for branch ``test``.

```
./manage.py dropdb test
```
