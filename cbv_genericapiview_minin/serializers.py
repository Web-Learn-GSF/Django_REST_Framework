from rest_framework import serializers
from fbv.models import BookInfo

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookInfo
        fields = '__all__'