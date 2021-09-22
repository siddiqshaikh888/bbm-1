from django.contrib import admin
from django.urls import path
from .views import AddPostView, HomeView, BlogDetailView #, UpdatePostView
from .views import *
 
urlpatterns = [
    path('', BlogListView, name='blogs'),
    path('<int:_id>', BlogDetailView, name='blog'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    #path('e/<int:_id>', UpdatePostView.as_view(), name='update_post'),
    #path('',HomeView.as_view(), name="home"),
]
