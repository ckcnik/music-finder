from django.shortcuts import render
from .tasks import download_video
from .forms import UrlSendForm
from django.http import HttpResponse


def index(request):
    """
    Главная страница
    """
    form = UrlSendForm(request.POST)

    if (request.method == 'POST' and form.is_valid()):
        url = form.cleaned_data['url']
        time = form.cleaned_data['time_start'] if form.cleaned_data['time_start'] else 0
        duration = form.cleaned_data['duration'] if form.cleaned_data['duration'] else 15

        # если урла есть, начинаем парсинг
        if url:
            url_obj = ParseUrl(url, time)

            # получаем объект - сайт
            site = get_object_or_404(Site, url=url_obj.domain, trash=False)
            # получаем объект - статус
            state = get_object_or_404(State, name=State.VIDEO_LOADING, trash=False)

            # оставляем запись в БД о запрошеннном видео
            video_obj = Video(uri=url_obj.uri, start_time=url_obj.time, site=site, state=state)
            video_obj.save()

            download_video.apply_async((video_obj, url, url_obj.time), queue='download_video')

    if request.is_ajax():
        return HttpResponse(video_obj.id)
    else:
        return render(request, 'mufi/index.html', {'form': form})
