"""keshihua URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from demo import views
from demo.views import login_view
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('demo.urls')),
    path('index/', views.IndexView.as_view()),
    path('', views.IndexView.as_view(),name="ind"),
    path('map', views.movieView.as_view()),
    path('temp', views.tempView.as_view()),
    path('graph', views.scoreView.as_view()),
    path('word', views.wordView.as_view()),
    path('login', login_view, name='login')
]
