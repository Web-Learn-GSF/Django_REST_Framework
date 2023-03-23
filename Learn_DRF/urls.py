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

# 随着版本更新，django建议使用path，但是仍然没有废除url
from django.urls import path, include
from django.urls import re_path as url

urlpatterns = [
    # fbv开发
    path('', include('fbv.urls')),
    
    # cbv_view开发
    path('', include('cbv_view.urls')),   
    
    # cbv_apiview开发
    path('', include('cbv_apiview.urls')),  
    
    # cbv_apiview_serializers开发
    path('', include('cbv_apiview_serializers.urls')),      
    
    # cbv_apiview_modelserializers开发
    path('', include('cbv_apiview_modelserializers.urls')),     
    
    # cbv_genericapiview_modelserializers开发
    path('', include('cbv_genericapiview_modelserializers.urls')),   
    
    # cbv_genericapiview_minin开发
    path('', include('cbv_genericapiview_minin.urls')),   
    
    # cbv_genericapiview_minin_repackaging开发
    path('', include('cbv_genericapiview_minin_repackaging.urls')), 
    
    # cbv_viewset开发
    path('', include('cbv_viewset.urls')),     
    
    
]
