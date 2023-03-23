from rest_framework import serializers
from fbv.models import BookInfo

class BookSerializer(serializers.ModelSerializer):

    # 若前端接口字典键不跟后端数据库一致，这样搞
    date = serializers.DateField(source='bpub_date')

    class Meta:
        model = BookInfo
        # fields = '__all__'
        exclude = ['bpub_date']