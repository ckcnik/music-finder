"""
В этот файл пихаем общие методы, классы для работы с вьюхами и моделями
"""
from urllib.parse import urlparse  # для разбивки урлы на отдельные части
from re import search
from requests import post
from base64 import b64encode
from music_finder.settings import MY_SETTING
from .models import Video, State
from os.path import getsize
import time
import hmac
import hashlib
import json


class ParseUrl(object):
    def __init__(self, url, time=0):
        """
        Распарсиваем урлу для сбора информации о видео-файле
        :param url:
        :param time: на случай, если врем попадет в гет-параметр основного запроса
        :return:
        """
        self.full_url = url
        parsed_uri = urlparse(url)  # разбиваем урлу на составляющие чтобы вытащить домен
        self.domain = parsed_uri.netloc
        if not time:
            result = search(r't=(\d+)$', url,)  # поиск временной метки в урле
            if result:
                time = int(result.group(1))
        self.time = time
        result = search(r'v=(([0-9]|[A-Z]|[a-z]|[-_])+)', url,)  # поиск uri видоса
        if result:
            video_uri = result.group(1)
        else:
            # для случая, если в сервис отправят сокращенную урлу - https://youtu.be/V_siccikiLU?t=19
            video_uri = parsed_uri.path[1:]  # берем без слеша (первый символ)
        self.uri = video_uri


def get_audio_content(file: Video):
    """
    Метод для идентификации аудио-файла
    :return:
    """
    file.set_state(State.SOUND_SEARCH)

    access_key = MY_SETTING['ACRCLOUD']['ACCESS_KEY']
    access_secret = MY_SETTING['ACRCLOUD']['ACCESS_SECRET']
    requrl = "http://ap-southeast-1.api.acrcloud.com/v1/identify"
    http_method = "POST"
    http_uri = "/v1/identify"
    data_type = "audio"
    signature_version = "1"
    timestamp = time.time()

    string_to_sign = http_method + "\n"+http_uri + "\n" + access_key + "\n" + data_type + "\n" + signature_version + "\n" + str(timestamp)

    sign = b64encode(hmac.new(access_secret.encode('utf-8'), string_to_sign.encode('utf-8'), digestmod=hashlib.sha1).digest())

    # suported file formats: mp3,wav,wma,amr,ogg, ape,acc,spx,m4a,mp4,FLAC, etc
    # File size: < 1M , You'de better cut large file to small file, within 15 seconds data size is better
    path = file.get_path_to_audio()
    f = open(path, "rb")
    sample_bytes = getsize(path)

    files = {'sample': f}
    data = {'access_key': access_key,
            'sample_bytes': sample_bytes,
            'timestamp': str(timestamp),
            'signature': sign,
            'data_type': data_type,
            "signature_version": signature_version}

    r = post(requrl, files=files, data=data)
    r.encoding = "utf-8"
    return json.loads(r.text)
