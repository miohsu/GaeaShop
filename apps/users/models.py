from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="male",
                              verbose_name="性别")
    email = models.CharField(max_length=128, null=True, blank=True, verbose_name="Email")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField(max_length=64, verbose_name='验证码')
    mobile = models.CharField(max_length=32, verbose_name="电话")
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "验证码"
        verbose_name_plural = "验证码"

    def __str__(self):
        return self.code
