from django.db import models
from django.utils import timezone
# Create your models here.

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
    # типы статусов (показывают этапы и состояния обратки видео)
    # STATE_TYPES = (
    #     ('1', 'video_loading'),  # выполняется загрузка видео
    #     ('2', 'video_loading_success'),  # загрузка видео выполнена успешно
    #     ('3', 'video_loading_error'),  # загрузка видео выполнена с ОШИБКОЙ
    #     ('4', 'sound_process'),  # выполняется обработка звука
    #     ('5', 'sound_process_success'),  # обработка звука выполнена успешно
    #     ('6', 'sound_process_error'),  # обработка звука выполнена с ОШИБКОЙ
    #     ('7', 'sound_search'),  # выполняется поиск названия аудио-трека
    #     ('8', 'sound_search_success'),  # поиск названия аудио-трека выполнен успешно
    #     ('9', 'sound_search_error'),  # поиск названия аудио-трека выполнен с ОШИБКОЙ
    # )
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