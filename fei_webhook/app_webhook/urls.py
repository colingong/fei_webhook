# from main_settings.urls import urlpatterns
from django.urls import path, include
from . import views
from . import views_github
from . import views_hhxx
from . import views_github_fei

urlpatterns = [
    path('', views.alive, name='alive'),
    path('github/', views_github.github_hook, name='webhook-github'),
    path('github/logs/<int:count>/', views_github.list_githublog, name='listlogs-github'),

    # for my local git server
    path('hhxx/', views_hhxx.hhxx_hook, name='webhook-hhxx'),

    # for github project fei
    path('fei/', views_github_fei.fei_project, name='project-fei'),
]