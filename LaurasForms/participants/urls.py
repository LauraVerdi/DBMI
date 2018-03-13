from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_participants, name='list_participants'),
    path('add', views.add_participant, name='add_participant'),
]