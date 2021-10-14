from django.urls import path

from . import views

urlpatterns = [
    path('timeline/', views.timeline, name = 'timeline'),
    path('detail/<int:post_id>/', views.detail, name = 'detail'),
    path('', views.index, name = 'index'),
]
