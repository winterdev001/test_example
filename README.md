# Application for Functional Testing in Django

This application allows users to register book information such as title and memo.

[![Image from Gyazo](https://i.gyazo.com/5b30d0b3287c0bb33ffe478559de5672.gif)](https://i.gyazo.com/5b30d0b3287c0bb33ffe478559de5672)

## Commands for building environment

```bash
pip install -r requirements.txt
createdb test_example
python manage.py migrate
python manage.py runserver
```

## Version used

```
asgiref==3.5.0
Django==4.0
psycopg2==2.8.6
sqlparse==0.4.2
tzdata==2022.1
```