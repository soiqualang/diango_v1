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

***

https://viblo.asia/p/python-co-ban-voi-django-framework-Ljy5VxGkZra

https://minhng.info/tutorials/hoc-django-trong-1-ngay.html

`python manage.py startapp book`

**Add app to setting**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api1',
    'book',
]
```

**Make model**
```python
class Category(models.Model):
   name = models.CharField(max_length=200)
   def __str__(self):
     return self.name

#Book model có field name, price, category, author_name
class Book(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField(default=0)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   author_name = models.CharField(max_length=200)
   def __str__(self):
     return self.name
```

**Migrate**

`python manage.py makemigrations book`

> Lưu trong thư mục migrations

**Check sql được tạo chính xác chưa**
`python manage.py sqlmigrate book 0001`

**Đẩy model vào DB**
> Mỗi `class` tương ứng là một `table`, mỗi `object` là một `record`

> Cái này gọi là ORM (Object-relational mapping)

`python manage.py migrate`

**Tạo user**

`python manage.py createsuperuser`
dtlong
dtlong

http://localhost:8000/admin/

## loop all in view
```html
{% for cat in categorys %}
    {{ cat.name }}
{% endfor %}
```

in view

```python
def index(request):
    #category_objs = Type.objects.filter(active__exact=True)
    categorys = Category.objects.all()
    return render(request, "cats.html", {'categorys': categorys})
```


## Preferece

https://medium.com/swlh/searching-in-django-rest-framework-45aad62e7782

https://medium.com/the-andela-way/creating-a-django-api-using-django-rest-framework-apiview-b365dca53c1d