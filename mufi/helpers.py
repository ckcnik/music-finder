from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Video, Site, State
from urllib.parse import urlparse  # для разбивки урлы на отдельные части
import re


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
            result = re.search(r't=(\d+)$', url,)  # поиск временной метки в урле
            if result:
                time = int(result.group(1))
        self.time = time
        result = re.search(r'v=(([0-9]|[A-Z]|[a-z]|[-_])+)', url,)  # поиск uri видоса
        if result:
            video_uri = result.group(1)
        else:
            # для случая, если в сервис отправят сокращенную урлу - https://youtu.be/V_siccikiLU?t=19
            video_uri = parsed_uri.path[1:]  # берем без слеша (первый символ)
        self.uri = video_uri
