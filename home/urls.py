from django.contrib import admin
from django.urls import path
from home import views
from .views import *

#from marketing import views

from django.contrib.auth import views as authview

urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    #path("blog/", views.blog, name='blog'),
    #path('blog/', views.BlogListView, name='blog'),
    path('sell/', views.sell, name='sell'),
    path('how_to_sell/', views.how_to_sell, name='how_to_sell'),
    
    #path('blog/<int:_id>', views.BlogDetailView, name='blog'),
    path("contact", views.contact, name='contact'),
    path("signup", views.handleSignup, name='handleSignup'),
    #path("login", views.handleLogin, name='handleLogin'),
    #path("logout", views.handleLogout, name='handleLogout'),
    path('change-password',authview.PasswordChangeView.as_view(template_name="change-password.html"),name='change-password'),
    path('password-change/',authview.PasswordChangeDoneView.as_view(template_name="change-password-done.html"),name='password_change_done'),
    #path("newsletter", views.newsletter, name='newsletter'),
    #path("videos", views.videos, name='videos'),
    path("search", views.search, name='search'),
    path("profile", views.profile, name='profile'),
    #path('newsletter',views.subscribe_to_newsletter, name="Subscribe-to-newsletter"),    
]
