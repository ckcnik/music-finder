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
Выполнить команду:<br>
``` $ sudo pip install django-celery ```<br>
<br>
В <b>settings.py</b> добвить строку<br>
``` INSTALLED_APPS += ("djcelery", ) ```

#### Установка Redis ####
Для установки redis выполнить следующие команды:<br>
``` $ sudo apt-get install redis-server ```<br>
``` $ sudo pi install redis```<br>
<br>
Проверка:<br>
``` $ redis-cli ping ```<br>
Ответ: `PONG`

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact