from django.db import models
from django.utils import timezone
from os.path import abspath  # для получения абсолютного пути
from pytube import YouTube  # парсер ютуб-роликов


class Site(models.Model):
    """
    Список сайтов из которых можно парсить видео-файлы
    """
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    trash = models.BooleanField(default=False)


class State(models.Model):
    """
    Возможные статусы обработок видео
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)
    trash = models.BooleanField(default=False)


class Video(models.Model):
    """
    Модель для хранения мета информации по загружаемым видео-файлам
    """
    uri = models.CharField(max_length=500)
    start_time = models.PositiveIntegerField(default=0)
    site = models.ForeignKey(Site)
    state = models.ForeignKey(State)
    date_created = models.DateTimeField(default=timezone.now)
    trash = models.BooleanField(default=False)
    # тут храним видосы
    PATH_TO_VIDEO = abspath(__file__) + '/../tmp/video/'

    def download(self, url):
        """
        Парсинг видео с ютуба
        :param url: урла с ютуба или еще откуда-то
        :return: возвращает true, если видео успешно загружено, в противном случае - возникнет исключение
        """
        yt = YouTube()
        yt.url = url
        video = yt.get('3gp', '144p', 'Simple')  # получаем видео в самом плохом качестве
        if not self.id:
            raise NameError('Не задан id для видеофайла!')
        video.filename = self.id
        video.download(self.PATH_TO_VIDEO)
        return True
