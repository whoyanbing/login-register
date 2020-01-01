from django.db import models

from login.models import User

# Create your models here.

class Type(models.Model):
    """视频类型模型定义"""
    # 分类id
    type_id = models.AutoField(primary_key=True, verbose_name='分类ID')
    # 类型名称
    type_name = models.CharField(verbose_name='分类名称', max_length=60, null=False)
    # 类型名称拼音
    type_en = models.CharField(max_length=60, null=False)
    # 排序id
    type_sort = models.PositiveSmallIntegerField(default=0)
    # 子类id
    type_mid = models.PositiveSmallIntegerField(default=1)
    # 父类id
    type_pid = models.PositiveSmallIntegerField(default=0)
    # 分类状态
    type_status = models.BooleanField(verbose_name='分类状态', default=1)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '视频分类'
        verbose_name_plural = '视频分类'

class Video(models.Model):
    """视频模型定义"""
    # 视频id
    vod_id = models.AutoField(verbose_name='视频ID', primary_key=True)
    # 视频分类id
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='视频分类')
    # 视频名称
    vod_name = models.CharField(verbose_name='视频名称', max_length=255, unique=True, null=False)
    # 视频名称扩展
    vod_sub = models.CharField(max_length=60)
    # 视频图片地址
    vod_pic = models.CharField(max_length=255, null=False)
    # 视频分类名称
    vod_class = models.CharField(verbose_name='视频分类',max_length=60, null=False)
    # 视频添加时间
    vod_time_add = models.DateTimeField(verbose_name='视频添加时间', auto_now_add=True)
    # 视频点击时间
    vod_time_hits = models.DateTimeField(auto_now=True)
    # 视频播放地址
    vod_play_url = models.CharField(max_length=255)
    # 视频作者
    vod_ower = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.vod_name

    class Meta:
        ordering = ['-vod_time_add']
        verbose_name = '视频列表'
        verbose_name_plural = '视频列表'