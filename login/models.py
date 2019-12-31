from django.db import models

# Create your models here.

class User(models.Model):

    """用户表定义"""
    gender = (
        ('male', '男'),
        ('female', '女')
    )
    # 用户姓名,必填,并且唯一,最长128字符
    name = models.CharField(max_length=128, unique=True)
    # 用户密码,密文
    password = models.CharField(max_length=256)
    # 用户邮箱
    email = models.EmailField(unique=True)
    # 用户性别
    sex = models.CharField(max_length=32, choices=gender, default='男')
    # 注册时间
    c_time = models.DateTimeField(auto_now_add=True)
    # 邮箱是否确认
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        # 人性化显示对象信息
        return self.name

    class Meta:
        # 就近显示
        ordering = ['-c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ':' + self.code

    class Meta:
        ordering = ['-c_time']
        verbose_name = '确认码'
        verbose_name_plural = '确认码'