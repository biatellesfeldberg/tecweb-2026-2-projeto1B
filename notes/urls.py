from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('tags/', views.tags, name='tags'),
    path('tags/<int:id>/', views.tag_detail, name='tag_detail'),
]