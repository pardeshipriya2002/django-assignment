from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_task/<int:uid>/', views.add_task, name='add_task'),
    path('export/', views.export_data, name='export_data')
    ]