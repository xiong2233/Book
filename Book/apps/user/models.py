from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
class Administrator(AbstractUser):
    username = models.CharField(max_length=150,unique=True,verbose_name="员工姓名")
    password = models.CharField(max_length=128,verbose_name="密码")
    is_active = models.BooleanField(default=True,verbose_name="是否激活")
    is_staff = models.BooleanField(default=False,verbose_name="是否为管理员")
    class Meta:
        verbose_name = "员工"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
class UserInfo(models.Model):
    email = models.EmailField(verbose_name="邮箱",unique=True)
    name = models.CharField(max_length=20,verbose_name="用户名",unique=True)
    code = models.CharField(max_length=8,verbose_name="验证码",default="nonu")
    is_active = models.BooleanField(default=False, verbose_name="是否激活")
    password = models.CharField(max_length=30,verbose_name="密码")
    phone_num = models.CharField(max_length=11,verbose_name="电话号码",null=True)
    money = models.DecimalField(default=0.00,max_digits=11,decimal_places=2,verbose_name="余额")
    birthday = models.DateField(verbose_name="出身日期",null=True)
    hobby = models.CharField(max_length=10,verbose_name="喜好书籍类型",null=True)
    say = models.CharField(max_length=200,verbose_name="格言",null=True)
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
# class borrow_book(models.Model):


