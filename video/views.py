from django.shortcuts import render
from django.views.generic import ListView, DetailView

from video.models import Video

# Create your views here.

class VideoList(ListView):
    model = Video
    template_name = 'video/video_list.html'

class VideoDetail(DetailView):
    model = Video
    queryset = Video.objects.all()
    template_name = 'video/video_detail.html'