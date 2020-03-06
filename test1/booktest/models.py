from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hage = models.IntegerField()
    hcomment = models.CharField(max_length=120)
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE,)

    def __str__(self):
        return self.hname

