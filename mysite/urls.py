from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as Auth_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('accounts/login/', Auth_views.LoginView.as_view(), name='login'),
    url(r'accounts/logout/', views.logout_view, name='logout'),
    url(r'', include('blog.urls'))
]
