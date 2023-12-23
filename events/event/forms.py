from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        strip=True,
        label='Название мероприятия'
    )
    description = forms.CharField(
        widget=forms.Textarea,
        strip=True,
        label='Описание мероприятия'
    )
    date_time = forms.DateTimeField(label='Дата и время', widget=forms.DateTimeInput)
    location = forms.CharField(
        max_length=100,
        strip=True,
        label='Местоположение'
    )

    class Meta:
        model = Event
        fields = 'title', 'description', 'date_time', 'location'
