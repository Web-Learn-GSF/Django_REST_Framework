from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(verbose_name='名称', max_length=20)
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(verbose_name='阅读量', default=0)
    bcomment = models.IntegerField(verbose_name='评论量', default=0)
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)
    
    class Meta:
        db_table = 'book_info'
        verbose_name = '图书'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.btitle