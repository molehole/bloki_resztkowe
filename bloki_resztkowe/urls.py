"""bloki_resztkowe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
app_name = 'bloki_resztkowe'

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wprowadz/', views.wprowadz_blok, name='wprowadz_blok'),
    path('nesting/new', views.nowy_nesting, name='nowy_nesting'),
    path('nesting/done', views.zakonczenie_nestingu, name='zakonczenie_nestingu'),
    path('pobierz/', views.pobierz_blok, name='pobierz_blok'),
    path('zaplanuj/', views.zaplanuj, name='zaplanuj'),
    path('<str:typ_zadania>/<str:pianka>', views.wybor, name='wybor'),
    path('', views.index, name='index'),
]
