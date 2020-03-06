from django.db import models

# Create your models here.
# test
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'