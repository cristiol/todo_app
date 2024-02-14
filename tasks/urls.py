from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete_task/<str:pk>/', views.delete_task, name='delete_task'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
]