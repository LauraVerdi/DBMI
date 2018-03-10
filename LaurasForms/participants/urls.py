from django.urls import path
from . import views

# app_name = 'LaurasForms'
urlpatterns = [
    path('', views.list_participants, name='list_participants'),
    path('add', views.add_participant, name='add_participant')
    # # ex: /DBMI/
    # path('', views.IndexView.as_view(), name='index'),
    # # ex: /DBMI/5/
    # path('<int:pk>/', views.InputView.as_view(), name='input'),
    # # ex: /DBMI/showall/
    # path('/showall/', views.ShowAllView.as_view(), name='showall'),
]