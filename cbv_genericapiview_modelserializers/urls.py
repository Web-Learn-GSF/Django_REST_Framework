"""Learn_DRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import re_path as url

from cbv_genericapiview_modelserializers import views

urlpatterns = [
    url(r'^books_genericapiview_modelserializers/$', views.Books_Genericapiview_ModelSerializers.as_view()),
    # 有名分组：P<pk>，会把pk当作参数，传递给get等请求
    url(r'^books_genericapiview_modelserializers/(?P<pk>\d+)$', views.Book_Genericapiview_ModelSerializers.as_view()),
]