# django tutorial

## Setup Repository

``` shell script
$ git clone https://github.com/kaito1002/django-tutorial.git && chmod a+x setup.sh && source setup.sh   # for python
$ git clone https://github.com/kaito1002/django-tutorial.git && chmod a+x setup.sh && source setup3.sh  # for python3
```

## Account

| column | value |
| :---: | :---: |
| user | admin |
| password | password |

## Scripts

### 開発サーバーの起動

```shell script
$ python manage.py runserver
```

### DBのマイグレーション

```shell script
$ python manage.py makemigrations && python manage.py migrate
```
