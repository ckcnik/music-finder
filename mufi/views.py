from django.shortcuts import render
from .tasks import download_video
from .forms import UrlSendForm


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
            download_video.apply_async((url, time), queue='download_video')
    if request.is_ajax():
        pass
    else:
        return render(request, 'mufi/index.html', {'form': form})
