from django.urls import path, include
from watch import views

app_name = 'watch'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
]







