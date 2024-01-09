from rest_framework import serializers
from fbv.models import *


class BookInfo_Serializers(serializers.ModelSerializer):

    class Meta:
        model = BookInfo
        fields = '__all__'