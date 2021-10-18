from django.urls import path
from django.conf.urls import include, url # real python tutorial

from . import views

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")), # real python
    url(r'^register/', views.register, name='register'),
    # real python
    path('home/', views.home, name = 'home'),
    path('detail/<int:post_id>/', views.detail, name = 'detail'),
    path('userhome/<str:user_name/', views.userpage, name = 'userhome'),
    path('', views.index, name = 'index'),
]
