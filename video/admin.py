from django.contrib import admin
from video import models

# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ['type_id', 'type_name', 'type_status']

admin.site.register(models.Type, TypeAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['vod_id', 'vod_name','vod_class' , 'vod_time_add']

admin.site.register(models.Video, VideoAdmin)
