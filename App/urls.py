from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    #path('add_item/<str:pk>/', views.add_item, name='add_item'),
    path('update/<pk>', views.edit_item, name='edititem'),
    path('delete_item/<str:pk>/', views.delete_item, name='delete_item'),
    #path('update_item/<str:pk>/', views.update_item, name='update_item'),

    #path('confirm_delete/<int:pk>/', views.confirm_delete, name='confirm_delete'),

    #path('new_search', views.new_search, name='new_search'),
]