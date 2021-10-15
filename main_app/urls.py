from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('detail/<int:post_id>/', views.detail, name = 'detail'),
    path('userhome/<str:user_name/', views.userpage, name = 'userhome'),
    path('', views.index, name = 'index'),
]
