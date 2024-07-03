from django.urls import path
from . import views
from .views import carrito_view
from  .views import crud_view
from django.contrib.auth import views as auth_views


urlpatterns = [path('', views.index,name='index'),
    path('login/', views.login_view, name='login'), 
    path('actividades', views.actividades_view, name= 'actividades'),
    path('restaurante', views.restaurante_view, name= 'restaurante'),
    path('habitaciones', views.habitaciones_view, name= 'habitaciones'),
    path('panel', views.panel_view, name= 'panel'),
    path('carrito', views.carrito_view, name='carrito'),
    path('crud', views.crud_view, name='crud'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('delete/<int:pk>/', views.delete_reserva, name='delete_reserva'),
    path('update/<int:pk>/', views.update_reserva, name='update_reserva'),


    







    ]