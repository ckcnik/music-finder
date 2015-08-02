from django.shortcuts import render, get_object_or_404
from .tasks import download_video
from .forms import UrlSendForm
from django.http import HttpResponse
from .helpers import ParseUrl
from .models import Site, State, Video
from json import dumps


def index(request):
    """
    Главная страница
    """
    data_request = False
    auto_submit = False  # авто-сабмит формы на случай отправки реквеста через гет-параметры
    if request.method == 'POST':
        data_request = request.POST
    elif request.method == 'GET':
        data_request = request.GET

    form = UrlSendForm(data_request)
    video_source_id = 0  # адишник записи видео-файла в БД

    if data_request and form.is_valid():
        if request.method == 'GET':
            auto_submit = True
        url = form.cleaned_data['url']
        time = form.cleaned_data['time_start'] if form.cleaned_data['time_start'] else 0
        duration = form.cleaned_data['duration'] if form.cleaned_data['duration'] else 15

        # если урла есть, начинаем парсинг
        if url:
            url_obj = ParseUrl(url, time)

            state = get_object_or_404(State, name=State.SOUND_SEARCH_SUCCESS, trash=False)
            videos = Video.objects.filter(uri=url_obj.uri, start_time__gte=(url_obj.time - 5),
                                          start_time__lte=(url_obj.time + 5), state=state).order_by('-date_created')
            if not len(list(videos.iterator())):
                # получаем объект - сайт
                site = get_object_or_404(Site, url=url_obj.domain, trash=False)
                # получаем объект - статус
                state = get_object_or_404(State, name=State.VIDEO_LOADING, trash=False)

                # оставляем запись в БД о запрошеннном видео
                video_obj = Video(uri=url_obj.uri, start_time=url_obj.time, site=site, state=state)
                video_obj.save()
                video_source_id = video_obj.id

                download_video.apply_async((video_obj, url, url_obj.time, duration), queue='download_video')
            else:
                video_obj = videos.last()
                video_source_id = video_obj.id

    if request.is_ajax():
        return HttpResponse(video_source_id)
    else:
        return render(request, 'mufi/index.html', {'form': form, 'auto_submit': auto_submit})


def checker_state(request):
    result = {'status': 'none'}
    if request.method == 'POST':
        video_id = request.POST['videoId']
        video = Video.objects.get(pk=video_id)
        if video.state.name == State.SOUND_SEARCH_SUCCESS:
            results = video.result_set.all()
            dict_array = [{'title': r.audio.title, 'artist': r.audio.artist, 'album': r.audio.album} for r in results]
            result = {'status': 'ok', 'songs': dict_array}
        elif video.state.name in (State.SOUND_PROCESS_ERROR, State.SOUND_SEARCH_ERROR, State.VIDEO_LOADING_ERROR):
            result = {'status': 'error'}
        else:
            result = {'status': 'pending'}

    return HttpResponse(dumps(result))


def yandex_verifi(request):
    """
    Верификация яндекс-вебмастера
    :param request:
    :return:
    """
    return render(request, 'mufi/yandex.html')
