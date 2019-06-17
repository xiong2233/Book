from django.db import models
from datetime import datetime
# Create your models here.
from user.models import UserInfo
from book_list.models import BookList
class UserOperation(models.Model):
    name = models.ForeignKey(UserInfo,verbose_name="用户")
    book_name = models.ForeignKey(BookList,verbose_name="书名")
    day = models.DateTimeField(default=datetime.now, verbose_name="借书时间")
    is_back = models.BooleanField(default=False,verbose_name="是否返还")
    class Meta:
        verbose_name = "租借书籍"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name.name

class UserReturnBook(models.Model):
    borrow = models.OneToOneField(UserOperation)
    backtime = models.DateTimeField(default=datetime.now,verbose_name="还书时间",)
    class Meta:
        verbose_name = "返还书籍"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.borrow.name.name
# ynolbwdylcpubcjb