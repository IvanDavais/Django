from django.db import models

# Create your models here.

class BookInfoManager(models.Manager):
    """ 图书模型管理器类 """
    # 1.改变查询的结构集
    def all(self):
        # 调用父类的all方法，获取所有的数据
        books = super().all() #QuerySet
        # 对数据进行过滤
        books = books.filter(isDelete=False)
        # 返回books
        return books
    
    # 封装函数：操作模型类对应的数据表(增删改查)
    def create_book(self, btitle, bpub_data):
        
        # 1.创建一个图书类
        # 使用 self.model()就可以创建一个跟自定义管理器对应的模型类对象
        model_class = self.model_class
        book = model_class()
        # book = BookInfo()
        book.btitle = btitle
        book.bpub_data = bpub_data
        # 2.保存进数据库
        book.save()
        # 3.返回book
        return book

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateField(auto_now=True)
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记，即删除数据库中的数据时，不做真正的删除 这种删除方式叫做软删除的标记
    isDelete = models.BooleanField(default=False)
    objects = BookInfoManager()

    class Meta:
        db_table = 'bookinfo' # 指定模型类对应的表名

class HeroInfo(models.Model):
    """ 英雄人物模型类 """
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=200)
    # 关系属性
    hbook = models.ForeignKey('BookInfo',on_delete='SET_DEFAULT')
    # 删除标记
    isDelete = models.BooleanField(default=False)



class AreaInfo(models.Model):
    """ 地区模型类 """
    atitle = models.CharField(max_length=20)
    # 关系属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self',blank=True, null=True,on_delete='SET_DEFAULT')