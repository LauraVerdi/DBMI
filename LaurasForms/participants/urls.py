from django.urls import path
from django.conf.urls import url
from . import views

# app_name = 'LaurasForms'
urlpatterns = [
    path('', views.list_participants, name='list_participants'),
    path('add', views.add_participant, name='add_participant'),
    # path('add/<pk>/verify', views.verify_participant, name='verify_participant'),
#    # path('verify/<pk>', views.verify_participant, name='verify_participant')
    # url(r'^verify/(?P<pk>\d+)/$', views.verify_participant, name='verify_participant')
    # # ex: /DBMI/
    # path('', views.IndexView.as_view(), name='index'),
    # # ex: /DBMI/5/
    # path('<int:pk>/', views.InputView.as_view(), name='input'),
    # # ex: /DBMI/showall/
    # path('/showall/', views.ShowAllView.as_view(), name='showall'),
]