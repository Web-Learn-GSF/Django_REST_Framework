from rest_framework.views import APIView

from django.http import JsonResponse

from fbv.models import BookInfo
from fbv import models

import json

from rest_framework import serializers
from rest_framework.response import Response

from cbv_apiview_modelserializers.serializers import BookSerializer


class Books_Apiview_ModelSerializers(APIView):
    '''获取所有和保存'''

    def get(self, request):
        # 查询图书对象
        books = BookInfo.objects.all()
        # 这一步并没有进行序列化
        ser = BookSerializer(instance=books, many=True)
        # ser.data才是进行了序列化，通过添加装饰器把data属性当作函数使用，ser.data就是将instance的内容进行序列化

        # 返回方式1：列表数据转JSON格式，需要添加safe=False
        # return JsonResponse(ser.data, safe=False)

        # 返回方式2：DRF的Response，牛的
        return Response(ser.data)
        '''ser.data函数的内容
            temp = []
            for obj in books:
                p = {}
                p['btitle'] = p.btitle
                p['bread'] = p.bread
                p['date'] = p.bpub_date
                
                temp.append(d)                
        '''

    def post(self, request):
        # 获取数据
        print(request.data)
        ser = BookSerializer(data=request.data)

        # 数据校验
        if ser.is_valid():  # is_valid()函数调用后才是做了校验，校验合格的数据存在ser.vaildated_data里面

            # # 手段1：常规手段
            # BookInfo.objects.create(**ser.validated_data)
            # return  Response(ser.data)

            # # 手段2：重写save方法，也是解耦的一个方式
            '''save函数源码，当传参instance的时候，调用update方法；没有传入的时候，调用create方法【均需要重写】
            if self.instance is not None:
                self.instance = self.update(self.instance, validated_data)
                
            else:
                self.instance = self.create(validated_data)
            '''
            ser.save()  # serializers文件里面重写create方法
            return Response(ser.data)

        else:
            return Response(ser.errors)


class Book_Apiview_ModelSerializers(APIView):
    '''获取单一和更新和删除'''

    def get(self, request, pk):
        # 查询数据对象：方法2
        # .filter 返回queryset对象
        # .get 返回模型类对象
        try:
            books = BookInfo.objects.get(id=pk)
        except:
            return Response({'errors': '错误信息, 数据不存在'}, status=400)

        ser = BookSerializer(instance=books, many=False)
        return Response(ser.data)

    def put(self, request, pk):
        # 获取数据
        book_data = request.data
        update_book = BookInfo.objects.get(id=pk)

        # 既要反序列化，校验；又要序列化，展示数据
        # 传入instance参数，才能保证调用的是update函数
        ser = BookSerializer(instance=update_book, data=book_data, many=False)

        # 验证数据:针对data=传入的数据
        if ser.is_valid():  # 验证成功的数据存入ser.validated_data里面，若有不对应的数据，就放在ser.errors里面
            ser.save()
            return Response(ser.data)

        else:
            Response(ser.errors)

    def delete(self, request, pk):

        # ！两种方法都是逻辑删除，没有删除该数据在数据库中的对应信息

        # # 方法1：save方法【非序列化的save方法】
        # try:
        #     delete_book = BookInfo.objects.get(id=pk)
        # except:
        #     return Response({'errors':'错误信息'}, status=400)

        # delete_book.is_delete = True
        # delete_book.save()

        # 方法2：update方法【非序列化的save方法中的update】
        delete_book = BookInfo.objects.filter(id=pk)
        if not delete_book:
            return Response({'errors': '错误信息'}, status=400)

        delete_book.update(is_delete=True)

        # 返回结果：表明已经存储成功
        return Response({})
