from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # # ex: /DBMI/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /DBMI/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /DBMI/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('input/', views.input, name ='input'),
    path('list/', views.list, name='list'),
]