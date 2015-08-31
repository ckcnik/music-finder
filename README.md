# README #

Приложение по идентификации аудиозаписей в интернете на видероликах YouTube

### MuFi - Music Finder ###

* Версия 1.0

### Установка ###

* Python 3.4
* PostgreSQL
* Зависимость от пакета - [PyTube](https://github.com/nficano/pytube)
* Зависимость от пакета - [Django celery](https://github.com/celery/django-celery/)
* Зависимость от пакета - [Redis](https://pypi.python.org/pypi/redis)

#### Установка Django celery ####
Выполнить команду:
```
#!bash
$ sudo pip install django-celery
```
В *settings.py* добвить строку
``` INSTALLED_APPS += ("djcelery", ) ```
Создать необходимые таблицы в БД
```
#!bash
$ python manage.py migrate
```

#### Установка Redis ####
Для установки redis выполнить следующие команды:
```
#!bash
$ sudo apt-get install redis-server
$ sudo pip install redis
```
Проверка:
```
#!bash
$ redis-cli ping
```
Ответ: `PONG`

### Virtual env ###
```
source env/bin/activate
```

### Запуск очередей ###
В папке с проектом выполнить комадну:
```
celery -A music_finder worker -l info -Q download_video,extract_audio,audio_identify
```

### Заупск сервера ###
```
gunicorn --bind=127.0.0.1:8888 --workers=3 --env DJANGO_SETTINGS_MODULE=music_finder.settings music_finder.wsgi
```
Ctrl + Z - приостановка процесса
fg - возобновить процесс
bg - запуск в фоне


### Поиск процесса ###
```
ps ax|grep gunicorn
```

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact