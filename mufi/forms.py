from django import forms
# from django.utils.translation import ugettext as _


class UrlSendForm(forms.Form):
    """
    Форма отправки данных на главной
    """
    url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Вставьте YouTube ссылку',
                                                       'class': 'form-control input-lg', 'type': 'search'}))
    time_start = forms.IntegerField(required=False, initial='0', widget=forms.TextInput(attrs={
        'class': "form-control", 'data-mask': "00:00:00"
    }), label='Начало')
    duration = forms.IntegerField(required=False, initial='15', widget=forms.HiddenInput())
