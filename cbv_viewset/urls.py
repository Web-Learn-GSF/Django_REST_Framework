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

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'books_viewset_pro_max', views.Books_Viewset_Pro_Max, basename='books_viewset_pro_max')

urlpatterns = [
    url(r'^books_viewset/$', views.Books_Viewset.as_view({
        'get': 'get_all',
        'post': 'add_object'
    })),
    # 有名分组：P<pk>
    url(r'^books_viewset/(?P<pk>\d+)$', views.Books_Viewset.as_view({
        'get': 'get_object',
        'put': 'update_object',
        'delete': 'delete_object'
    })),
    url(r'^books_viewset_pro/$', views.Books_Viewset_Pro.as_view({
        'get': 'list',
        'post': 'create'
    })),
    # 有名分组：P<pk>
    url(r'^books_viewset_pro/(?P<pk>\d+)$', views.Books_Viewset_Pro.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

    # url(r'^books_viewset_pro_max/$', views.Books_Viewset_Pro_Max.as_view({'get':'list', 'post':'create'})),
    # # 有名分组：P<pk>
    # url(r'^books_viewset_pro_max/(?P<pk>\d+)$', views.Books_Viewset_Pro_Max.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
]

urlpatterns += router.urls