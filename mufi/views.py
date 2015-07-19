from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Video, Site, State
from .helpers import ParseUrl


def index(request):
    """
    Главная страница
    """
    url = request.GET.get('url', '')
    time = int(request.GET.get('t', 0))  # на случай, если врем попадет в гет-параметр основного запроса
    url_obj = ParseUrl(url, time)

    # если урла есть, начинаем парсинг
    if url:
        # получаем объект - сайт
        site = get_object_or_404(Site, url=url_obj.domain, trash=False)
        # получаем объект - статус
        state = get_object_or_404(State, name='video_loading', trash=False)

        # оставляем запись в БД о запрошеннном видео
        video_obj = Video(uri=url_obj.uri, start_time=url_obj.time, site=site, state=state)
        video_obj.save()

        # если видео успешно скачано
        if video_obj.download(url):
            state = get_object_or_404(State, name='video_loading_success', trash=False)
            video_obj.state = state
            video_obj.save()
    return HttpResponse(time)