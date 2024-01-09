# from django.views import View
from rest_framework.views import APIView
#from django.http import JsonResponse
from rest_framework.response import Response
from fbv.models import BookInfo
import json
from .serializers import *


class BooksView_apiview(APIView):
    """实现查询和新增书籍功能
            1. 查询所有书籍信息
            2. 新增书籍信息
    """
    '''功能1：查询所有书籍'''

    def get(self, request):

        books = BookInfo.objects.all()
        ser = BookInfo_Serializers(books, many=True)

        return Response(ser.data)

    '''功能2：新增书籍信息'''

    def post(self, request):

        ser = BookInfo_Serializers(data=request.data)
        resp = {}
        if ser.is_valid():
            ser.save()
            resp['code'] = 201
            resp['code'] = ser.data
        else:
            print(ser.errors)
            resp['code'] = 401
            resp['code'] = ser.errors
        return Response(resp)


class BookView_apiview(APIView):
    """实现删、改、查书籍功能
            1. 查询单一书籍信息
            2. 修改现有书籍信息
            3. 删除某一书籍信息
    """

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass