from django.urls import path, include
from watch import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
]







