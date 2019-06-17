from django.db import models

# Create your models here.

class BookCategory(models.Model):
    category = models.CharField(verbose_name="类别",max_length=50)
    class Meta:
        verbose_name = "书籍类别"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.category

class BookList(models.Model):
    name = models.CharField(verbose_name="书名",max_length=50)
    author = models.CharField(verbose_name="作者",max_length=30)
    press = models.CharField(verbose_name="出版社",max_length=100)
    category = models.ForeignKey(BookCategory,verbose_name="类别")
    num = models.IntegerField(default=0,verbose_name="库存")
    price = models.DecimalField(default=0.00,decimal_places=2,max_digits=11)
    image = models.ImageField(verbose_name="图片",upload_to="static/images/goods/", null=True)
    class Meta:
        verbose_name = "书籍清单"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
