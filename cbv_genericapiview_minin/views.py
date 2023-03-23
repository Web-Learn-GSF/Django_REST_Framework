from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

from django.http import JsonResponse

from fbv.models import BookInfo
from fbv import models

import json

from rest_framework import serializers
from rest_framework.response import Response

from cbv_genericapiview_minin.serializers import BookSerializer


class Books_Genericapiview_Minin(ListModelMixin, CreateModelMixin, GenericAPIView):
    # GenericAPIView规定要写的类属性
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer
    
    '''获取所有和保存'''
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
            
            
# 找寻方法也是从左到右，继承顺序很关键
class Book_Genericapiview_Minin(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer
    
    # 自定义destory函数，改变删除逻辑
    def destroy(self, request, pk):
        books = self.get_object()
        books.is_delete = True
        books.save()
        return Response({})
    
    '''获取单一和更新和删除'''
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    # Minin里面定义的delete是物理删除
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
