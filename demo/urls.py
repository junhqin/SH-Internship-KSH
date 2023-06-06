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
from django.urls import path
from . import views

urlpatterns = [
    path('ssrd/', views.ssrd1.as_view(), name='ssrd'), # 实时热点
    path('update/',views.update1.as_view(),name='update'),#最后更新时间
    path('avg_salary/',views.avg_salary1.as_view(),name='avg_salary'),
    path('lan_fre/',views.lan_fre1.as_view(),name='lan_fre'),
    path('job_fre/',views.job_fre1.as_view(),name='job_fre'),
    path('g4/', views.g4.as_view(), name='g4'),
    path('sankey/', views.sankey.as_view(), name='sankey')
]
