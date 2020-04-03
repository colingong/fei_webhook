# from main_settings.urls import urlpatterns
from django.urls import path, include
from . import views
from . import views_github
urlpatterns = [
    path('', views.alive, name='alive'),
    path('github/', views_github.webhook, name='webhook-github'),
]