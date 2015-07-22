from django.contrib import admin
from .models import Site, Video, State


class SiteAdmin(admin.ModelAdmin):
    """
    добавил в админку модель сайтов (будем вручную добавлять/удалять
    поддерживаемые для парсинга сайты)
    """
    # fields = ['name', 'date_created']
    list_display = ('name', 'url', 'date_created', 'trash')
admin.site.register(Site, SiteAdmin)


class StateAdmin(admin.ModelAdmin):
    """
    добавил в админку модель статусов по обработке видосов
    """
    # fields = ['name', 'date_created', 'trash']
    list_display = ('name', 'description', 'date_created', 'trash')
admin.site.register(State, StateAdmin)


class VideoAdmin(admin.ModelAdmin):
    """
    добавил в админку модель видосов (стата по запрашиваемым видео)
    """
    # fields = ['uri', 'start_time', 'site', 'state', 'date_created', 'trash']
    list_display = ('id', 'uri', 'start_time', 'get_site_url', 'get_state', 'date_created', 'trash')

    def get_site_url(self, obj):
        return obj.site.url
    get_site_url.short_description = 'Урла'

    def get_state(self, obj):
        return obj.state.description
    get_state.short_description = 'Статус'
admin.site.register(Video, VideoAdmin)