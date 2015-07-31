import time

from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404
from os import system, remove
from os.path import abspath, dirname, isfile
from pytube import YouTube  # парсер ютуб-роликов
from youtube_dl import YoutubeDL
from music_finder.settings import DOWN_LOADER


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

    # константы состояний, они забиты в таблицу и помещены в код только для ясности
    VIDEO_LOADING = 'video_loading'
    VIDEO_LOADING_SUCCESS = 'video_loading_success'
    VIDEO_LOADING_ERROR = 'video_loading_error'
    SOUND_PROCESS = 'sound_process'
    SOUND_PROCESS_SUCCESS = 'sound_process_success'
    SOUND_PROCESS_ERROR = 'sound_process_error'
    SOUND_SEARCH = 'sound_search'
    SOUND_SEARCH_SUCCESS = 'sound_search_success'
    SOUND_SEARCH_ERROR = 'sound_search_error'


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
    PATH_TO_VIDEO = dirname(abspath(__file__)) + '/tmp/video/'
    # временные аудио-файлы
    PATH_TO_AUDIO = dirname(abspath(__file__)) + '/tmp/audio/'
    # время длительности аудиофайла
    DURATION_SOUND_FILE = 15
    # единый формат аудио-файлов с которым мы работаем
    AUDIO_FILE_FORMAT = '.mp3'
    # единый формат видео-файлов с которым мы работаем
    VIDEO_FILE_FORMAT = '.3gp'

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

    def download_dl(self, url):
        """
        Парсинг видео с ютуба через youtube-dl
        :param url: урла с ютуба или еще откуда-то
        :return: возвращает true, если видео успешно загружено, в противном случае - возникнет исключение
        """

        if not self.uri:
            raise NameError('Не задан id для видеофайла!')

        pathToFile = self.PATH_TO_VIDEO + str(self.uri)
        options = {
            'format': 'bestaudio/best',  # choice of quality
            'extractaudio': True,  # only keep the audio
            'audioformat': "mp3",  # convert to mp3
            'outtmpl': self.PATH_TO_VIDEO + str(self.uri),  # name the file the ID of the video
            'noplaylist': True,  # only download single song, not playlist
        }

        if not isfile(pathToFile):
            with YoutubeDL(options) as ydl:
                ydl.download([url])
        return True

    def extract_audio(self, seconds=0, duration=DURATION_SOUND_FILE):
        """
        Извлечение указанного промежутка аудио-потока из видео-файла и
        загрузка его во временный аудио-файл
        :param seconds: позиция старта (в секундах), по умолчанию с начала
        :param duration: длительность (в секундах), по умолчанию 30 с.
        :return: возвращает True если файл создан, иначе - False
        возвращает исключение если не существует видео-файла источника
        """
        self.set_state('sound_process')

        video_file_path = self.get_path_to_video(True) if DOWN_LOADER == 'ydl' else self.get_path_to_video()
        audio_file_path = self.get_path_to_audio()

        if not isfile(video_file_path):
            self.set_state('sound_process_error')
            raise NameError('Видое-файл не существует!')

        start = time.strftime("%H:%M:%S", time.gmtime(seconds))
        duration = time.strftime("%H:%M:%S", time.gmtime(duration))

        ffmpeg_cmd = 'ffmpeg -i {0} -ss {1} -t {2} -acodec libmp3lame -aq 4 {3}'.format(video_file_path, start, duration, audio_file_path)
        system(ffmpeg_cmd)

        return isfile(audio_file_path)

    def set_state(self, name):
        """
        Запись статуса в БД
        :param name:
        :return: None
        """
        state = get_object_or_404(State, name=name, trash=False)
        self.state = state
        self.save()

    def get_path_to_audio(self, without_format=False):
        """
        Возвращает путь к аудио-файлу
        :return:
        """
        path = self.PATH_TO_AUDIO + str(self.id)
        if not without_format:
            path += self.AUDIO_FILE_FORMAT
        return path

    def get_path_to_video(self, without_format=False):
        """
        Возвращает путь к видео-файлу
        :return:
        """
        path = self.PATH_TO_VIDEO + str(self.uri)
        if not without_format:
            path += self.VIDEO_FILE_FORMAT
        return path
    
    def remove_video_file(self):
        """
        Удаление временного видео-файла
        :return: None
        """
        remove(self.get_path_to_video(True) if DOWN_LOADER == 'ydl' else self.get_path_to_video())

    def remove_audio_file(self):
        """
        Удаление временного видео-файла
        :return: None
        """
        remove(self.get_path_to_audio())


class Audio(models.Model):
    """
    Список аудио-записей
    """
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    acrid = models.CharField(max_length=32)
    date_created = models.DateTimeField(default=timezone.now)
    trash = models.BooleanField(default=False)


class Result(models.Model):
    """
    Модель для хранения результатов поиска
    """
    video = models.ForeignKey(Video)
    audio = models.ForeignKey(Audio, null=True)
    response = models.PositiveIntegerField(default=0)
    play_offset = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    trash = models.BooleanField(default=False)
