from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'webapp'

urlpatterns = [
    path('lyrics/', views.LyricsList.as_view()),
    path('lyrics/<int:pk>/', views.LyricsDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
]
 
 