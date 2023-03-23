from rest_framework.generics import GenericAPIView
from django.http import JsonResponse

from fbv.models import BookInfo
from fbv import models

import json

from rest_framework import serializers
from rest_framework.response import Response

from cbv_genericapiview_modelserializers.serializers import BookSerializer


class Books_Genericapiview_ModelSerializers(GenericAPIView):
    
    # GenericAPIView规定要写的类属性
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer
    
    '''获取所有和保存'''
    def get(self, request):
        
        # # 原始方法
        # books = BookInfo.objects.all()
        # ser = BookSerializer(instance=books, many=True)
        
        # # GenericAPIView封装方法：1
        # books = self.get_queryset()
        # ser = self.get_serializer_class()(instance=books, many=True)
        
        # GenericAPIView封装方法：2
        ser = self.get_serializer(instance=self.get_queryset(), many=True)

        return Response(ser.data)    

    
    
    def post(self, request):
        
        '''many=True所造成的错误： 
                "non_field_errors": [
                    "Expected a list of items but got type \"dict\"."
                ]   
        '''
        ser = self.get_serializer(data=request.data, many=False)
        
        if ser.is_valid():
            ser.save()
            return  Response(ser.data) 
        
        else:
            return Response(ser.errors)
            
            
    
    
class Book_Genericapiview_ModelSerializers(GenericAPIView):
    
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer
    
    '''获取单一和更新和删除'''
    def get(self, request, pk):

        # # 方法1：常规
        # try:
        #     books = BookInfo.objects.get(id=pk)
        # except:
        #     return Response({'errors':'错误信息, 数据不存在'}, status=400)
        
        # ser = self.get_serializer(instance=books, many=False)

        
        # 方法2：self.get_object()，是一个基于有名分组的pk：(?P<pk>\d+)$，然后获取单个对象
        ser = self.get_serializer(instance=self.get_object(), many=False)

        return Response(ser.data)  
    
    
    def put(self, request, pk):

        ser = self.get_serializer(instance=self.get_object(), data=request.data, many=False)
        if ser.is_valid():
            ser.save()
            return  Response(ser.data)
        else:
            return Response(ser.errors)

    
    def delete(self, request, pk):
        
        # ！逻辑删除，没有删除该数据在数据库中的对应信息
        
        # # 这样不行：这种情况下，save的对象不是第一行对应的对象
        # self.get_object().is_delete = True    
        # self.get_object().save()
        
        books = self.get_object()
        books.is_delete = True
        books.save()
        
        
        # ！物理删除，删除该数据在数据库中的对应信息，即对应id删除
        # self.get_object().delete()
        
        return Response({})
    
    
