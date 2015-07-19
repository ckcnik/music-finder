from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Video, Site, State
from urllib.parse import urlparse  # для разбивки урлы на отдельные части
import re


def index(request):
    """
    Главная страница
    """
    url = request.GET.get('url', '')
    parsed_uri = urlparse(url)  # разбиваем урлу на составляющие чтобы вытащить домен
    time = int(request.GET.get('t', 0))  # на случай, если врем попадет в гет-параметр основного запроса
    if time == 0:
        result = re.search(r't=(\d+)$', url,)  # поиск временной метки в урле
        if result:
            time = int(result.group(1))
    result = re.search(r'v=(([0-9]|[A-Z]|[a-z]|[-_])+)', url,)  # поиск uri видоса
    if result:
        video_uri = result.group(1)
    else:
        # для случая, если в сервис отправят сокращенную урлу - https://youtu.be/V_siccikiLU?t=19
        video_uri = parsed_uri.path[1:]  # берем без слеша (первый символ)

    # если урла есть, начинаем парсинг
    if url:
        # получаем объект - сайт
        site = get_object_or_404(Site, url=parsed_uri.netloc, trash=False)
        # получаем объект - статус
        state = get_object_or_404(State, name='video_loading', trash=False)

        # оставляем запись в БД о запрошеннном видео
        video_obj = Video(uri=video_uri, start_time=time, site=site, state=state)
        video_obj.save()

        # если видео успешно скачано
        if video_obj.download(url):
            state = get_object_or_404(State, name='video_loading_success', trash=False)
            video_obj.state = state
            video_obj.save()
    return HttpResponse(time)