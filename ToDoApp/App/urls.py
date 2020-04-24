from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
    #path('confirm_delete/<int:pk>/', views.confirm_delete, name='confirm_delete'),

    #path('new_search', views.new_search, name='new_search'),
]