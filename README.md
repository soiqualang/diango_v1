# diango_v1
Test with diango

## Install Diango
`pip install django`

## Make project
`django-admin startproject app1`

## Start webserver
`python manage.py runserver`

```bash
Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver

(diango_v1) D:\programing\py360\diango_v1\project\app1>
```

## Err connect to PostgreSQl
`django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 module: No module named 'psycopg2'`

> `psycopg2`
> `psycopg2-binary`

## Migrate Db to Other DBMS
> `python manage.py makemigrations`
> `python manage.py migrate`

***

## Start a sub app/service
`python manage.py startapp api1`



