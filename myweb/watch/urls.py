from django.urls import path, include
from watch import views

app_name = 'watch'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('category/<str:category>/', views.index, name='category-list'),
]







