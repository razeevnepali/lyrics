from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('lyrics/', views.LyricsList.as_view()),
    path('lyrics/<int:pk>/', views.LyricsDetail.as_view()),
]
 
 