from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('room/<int:room_id>', views.room, name='room'),
    path('create/', views.create, name='create'),
    path('delete/<int:room_id>', views.delete, name='delete'),
    path('edit/<int:room_id>', views.edit, name='edit'),
]