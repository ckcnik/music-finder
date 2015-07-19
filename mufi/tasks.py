from celery import task
from celery.utils.log import get_task_logger
from django.shortcuts import get_object_or_404
from .models import Video, Site, State
from .helpers import ParseUrl, get_audio_content

logger = get_task_logger(__name__)


@task(name='download video')
def download_video(url, time):
    url_obj = ParseUrl(url, time)

    # получаем объект - сайт
    site = get_object_or_404(Site, url=url_obj.domain, trash=False)
    # получаем объект - статус
    state = get_object_or_404(State, name=State.VIDEO_LOADING, trash=False)

    # оставляем запись в БД о запрошеннном видео
    video_obj = Video(uri=url_obj.uri, start_time=url_obj.time, site=site, state=state)
    video_obj.save()

    # если видео успешно скачано
    result = video_obj.download(url)
    if result:
        video_obj.set_state(State.VIDEO_LOADING_SUCCESS)
        extract_audio.apply_async((video_obj, url_obj), queue='extract_audio')
    else:
        video_obj.set_state(State.VIDEO_LOADING_ERROR)
    return result


@task(name='extract audio')
def extract_audio(video_obj, url_obj):
    # если успешно извлечен аудио-поток
    result = video_obj.extract_audio(url_obj.time)
    if result:
        video_obj.set_state(State.SOUND_PROCESS_SUCCESS)
        audio_identify.apply_async((video_obj,), queue='audio_identify')
        video_obj.remove_video_file()
    else:
        video_obj.set_state(State.SOUND_PROCESS_ERROR)
    return result


@task(name='audio identify')
def audio_identify(video_obj):
    request = get_audio_content(video_obj)
    if request['status']['msg'] == 'Success':
        video_obj.set_state(State.SOUND_SEARCH_SUCCESS)
        video_obj.remove_audio_file()
        logger.info(request)
    else:
        video_obj.set_state(State.SOUND_SEARCH_ERROR)