from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checker_state/$', views.checker_state, name='checker_state'),
    url(r'^yandex_5c9fac42e7f6e558\.html$',views.yandex_verifi, name='yandex_verifi'),
]