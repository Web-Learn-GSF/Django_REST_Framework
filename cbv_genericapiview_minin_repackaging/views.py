from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django.http import JsonResponse

from fbv.models import BookInfo
from fbv import models

import json

from rest_framework import serializers
from rest_framework.response import Response

from cbv_genericapiview_minin_repackaging.serializers import BookSerializer


class Books_Genericapiview_Minin_Repackaging(ListCreateAPIView):
    # GenericAPIView规定要写的类属性
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer
    
            
    
class Book_Genericapiview_Minin_Repackaging(RetrieveUpdateDestroyAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer
    
    # 自定义destory函数，改变删除逻辑
    def destroy(self, request, pk):
        books = self.get_object()
        books.is_delete = True
        books.save()
        return Response({})
    
    
