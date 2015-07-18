from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube
import os


def index(request):
    url = request.GET.get('url', '')

    yt = YouTube()
    yt.url = url
    video = yt.get('3gp', '144p', 'Simple')  # получаем видео в самом плохом качестве
    video.download(os.path.abspath(__file__) + '/../tmp/video')
    return HttpResponse(print(yt.videos))