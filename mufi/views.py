from django.shortcuts import render
from .tasks import download_video


def index(request):
    """
    Главная страница
    """
    url = request.GET.get('url', '')

    # если урла есть, начинаем парсинг
    if url:
        time = int(request.GET.get('t', 0))  # на случай, если врем попадет в гет-параметр основного запроса
        download_video.apply_async((url, time), queue='download_video')

    return render(request, 'mufi/index.html')
