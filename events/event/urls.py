from django.urls import path

from . import views

app_name = 'event'
urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('events/<int:id>/delete', views.event_delete, name='event_delete'),
    path('events/<int:id>/edit', views.event_edit, name='event_edit'),
    path('events/<int:id>', views.event_detail, name='event_detail'),
]
