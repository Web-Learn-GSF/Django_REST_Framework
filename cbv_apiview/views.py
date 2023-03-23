# from django.views import View
from rest_framework.views import APIView

from django.http import JsonResponse

from fbv.models import BookInfo
from fbv import models

import json


class BooksView_apiview(APIView):
    """实现查询和新增书籍功能
            1. 查询所有书籍信息
            2. 新增书籍信息
    """
    '''功能1：查询所有书籍'''
    def get(self, request):
        
        books = BookInfo.objects.all()
        
        book_list = []
        for book in books:
            book_list.append({'id':book.id,
                              'btitle':book.btitle,
                              'bpub_date':book.bpub_date,
                              'bread':book.bread,
                              'bcomment':book.bcomment
                              })
            
        # 列表数据转JSON格式，需要添加safe=False
        return JsonResponse(book_list, safe=False)
    
    '''功能2：新增书籍信息'''
    def post(self, request):

        data = request.body.decode()
        data_dict = json.loads(data)

        print(type(request.body), type(request.body.decode()), type(data_dict))
        
        # 验证数据
        btitle = data_dict.get('btitle')
        bpub_date = data_dict.get('bpub_date')
        if btitle is None or bpub_date is None:
            return JsonResponse({'errors':'错误信息'}, status=400)
    
        # 保存数据
        book = BookInfo.objects.create(btitle=btitle, bpub_date=bpub_date)
        
        # 返回结果：表明已经存储成功
        return JsonResponse({ 'id':book.id,
                              'btitle':book.btitle,
                              'bpub_date':book.bpub_date,
                              'bread':book.bread,
                              'bcomment':book.bcomment
                              })
        
        
class BookView_apiview(APIView):
    """实现删、改、查书籍功能
            1. 查询单一书籍信息
            2. 修改现有书籍信息
            3. 删除某一书籍信息
    """
    def get(self, request, pk):
        # # 查询数据对象：方法1【忘了什么类对象无匹配结果，返回异常】
        # try:
        #     book = BookInfo.objects.get(id=pk)
        # except:
        #     return JsonResponse({'errors':'错误信息'}, status=400)
        
        # return JsonResponse({ 'id':book.id,
        #                       'btitle':book.btitle,
        #                       'bpub_date':book.bpub_date,
        #                       'bread':book.bread,
        #                       'bcomment':book.bcomment
        #                       })        
        
        
        # 查询数据对象：方法2【模型类对象匹配无结果，返回为空】
        book = models.BookInfo.objects.filter(id=pk).first()
        
        if not book:
            return JsonResponse({'errors':'错误信息'}, status=400)
        
        return JsonResponse({ 'id':book.id,
                              'btitle':book.btitle,
                              'bpub_date':book.bpub_date,
                              'bread':book.bread,
                              'bcomment':book.bcomment
                              })          
    
    
    def put(self, request, pk):
        # 获取数据
        data = request.body.decode()
        data_dict = json.loads(data)
        
        # 验证数据
        btitle = data_dict.get('btitle')
        bpub_date = data_dict.get('bpub_date')
        if btitle is None or bpub_date is None:
            return JsonResponse({'errors':'错误信息'}, status=400)
    
        # 保存数据
        book = models.BookInfo.objects.filter(id=pk)
        if not book:
            return JsonResponse({'errors':'错误信息'}, status=400)
        
        book.update(btitle=btitle, bpub_date=bpub_date)
        
        book = book.first()
        # 返回结果：表明已经存储成功
        return JsonResponse({ 'id':book.id,
                              'btitle':book.btitle,
                              'bpub_date':book.bpub_date,
                              'bread':book.bread,
                              'bcomment':book.bcomment
                              })
    
    def delete(self, request, pk):
        # 获取数据
        print(type(request.body))
        
        data = request.body.decode()
        data_dict = json.loads(data)
        
        # 验证数据
        book = models.BookInfo.objects.filter(id=pk)
        if not book:
            return JsonResponse({'errors':'错误信息'}, status=400)
        
        # 物理删除：删除对应的id信息，从数据库中抹除
        # book.delete()
        
        # 逻辑删除：信息依旧存储在数据库里面，只是对应是否删除的信息=True
        book.update(is_delete=True)
        
        # 返回结果：表明已经存储成功
        return JsonResponse({})
    