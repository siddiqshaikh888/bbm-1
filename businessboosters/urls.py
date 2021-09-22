"""businessboosters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views

from core.views import frontpage, signup

admin.site.site_header = "Business Boosters Admin"
admin.site.site_title = "Business Boosters Admin Portal"
admin.site.index_title = "Welcome to Business Boosters Market"

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    #path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('dashboard/', include('userprofile.urls')),
    path('notifications/', include('notification.urls')),
    path('products/', include('product.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blogapp.urls'))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
