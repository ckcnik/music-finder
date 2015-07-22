from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checker_state$', views.checker_state, name='checker_state'),
]