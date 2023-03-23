from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet
from rest_framework.decorators import action

from django.http import JsonResponse

from fbv.models import BookInfo
from fbv import models

import json

from rest_framework import serializers
from rest_framework.response import Response

from .serializers import BookSerializer


class Books_Viewset(ViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer

    def get_all(self, request):
        pass

    def add_object(self, request):
        pass

    def get_object(self, request, pk):
        pass

    def update_object(self, request, pk):
        pass

    def delete_object(self, request, pk):
        pass


class Books_Viewset_Pro(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer


class Books_Viewset_Pro_Max(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer

    @action(methods=['get'], detail=False, url_path='login')
    def login(self, request):
        """登录"""
        return Response({'message': '成功！！'})
