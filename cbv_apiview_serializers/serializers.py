from rest_framework import serializers
from fbv.models import BookInfo


class BookSerializer(serializers.Serializer):
    # 序列化返回字段
    btitle = serializers.CharField()
    bread = serializers.IntegerField()

    # 若前端接口字典键不跟后端数据库一致，这样搞
    date = serializers.DateField(source='bpub_date')

    def create(self, validated_data):
        new_book = BookInfo.objects.create(**validated_data)

        # 结果返回给了ser.instance
        return new_book

    def update(self, instance, validated_data):
        BookInfo.objects.filter(id=instance.pk).update(**validated_data)
        updated_book = BookInfo.objects.get(id=instance.pk)

        # 结果返回给了ser.instance
        return updated_book
