from celery import task
from celery.utils.log import get_task_logger
from django.db import transaction
from .models import State, Result, Audio
from .helpers import get_audio_content
from music_finder.settings import DOWN_LOADER

logger = get_task_logger(__name__)


@task(name='download video')
def download_video(video_obj, url, time, duration):
    # если видео успешно скачано
    result = video_obj.download_dl(url) if DOWN_LOADER == 'ydl' else video_obj.download(url)
    if result:
        video_obj.set_state(State.VIDEO_LOADING_SUCCESS)
        extract_audio.apply_async((video_obj, time, duration), queue='extract_audio')
    else:
        video_obj.set_state(State.VIDEO_LOADING_ERROR)
    return result


@task(name='extract audio')
def extract_audio(video_obj, time, duration):
    # если успешно извлечен аудио-поток
    result = video_obj.extract_audio(time, duration)
    if result:
        video_obj.set_state(State.SOUND_PROCESS_SUCCESS)
        # video_obj.remove_video_file() # todo: повесить удаление файлов по крону
        audio_identify.apply_async((video_obj,), queue='audio_identify')
    else:
        video_obj.set_state(State.SOUND_PROCESS_ERROR)
    return result


@task(name='audio identify')
def audio_identify(video_obj):
    response = get_audio_content(video_obj)
    metadata = response['metadata'] if 'metadata' in response else []
    # video_obj.remove_audio_file()

    empty_result = False
    with transaction.atomic():
        music = metadata['music'] if 'music' in metadata else []
        for info in music:
            if 'title' in info.keys():
                audio = Audio.objects.filter(acrid=info['acrid'], trash=False)
                if not audio:
                    audio = Audio(title=info['title'], artist=info['artists'][0]['name'], album=info['album']['name'], acrid=info['acrid'])
                    audio.save()
                else:
                    audio = audio[0]
                result = Result(video=video_obj, audio=audio, response=response['status']['code'], play_offset=info['play_offset_ms'])
                result.save()
            else:
                empty_result = True

    if response['status']['code'] == 0 and not empty_result:
        video_obj.set_state(State.SOUND_SEARCH_SUCCESS)
    else:
        video_obj.set_state(State.SOUND_SEARCH_ERROR)

    return response['status']['msg']
