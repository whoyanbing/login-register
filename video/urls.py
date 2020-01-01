from django.urls import path
from video import views

urlpatterns = [
    path('index', views.VideoList.as_view()),
    path('watch/<int:pk>', views.VideoDetail.as_view())
]