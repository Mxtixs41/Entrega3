from django.urls import path
from . import views
from .views import carrito_view
from  .views import crud_view

urlpatterns = [path('', views.index,name='index'),
    path('login/', views.login_view, name='login'), 
    path('actividades', views.actividades_view, name= 'actividades'),
    path('restaurante', views.restaurante_view, name= 'restaurante'),
    path('habitaciones', views.habitaciones_view, name= 'habitaciones'),
    path('panel', views.panel_view, name= 'panel'),
    path('carrito', carrito_view, name='carrito'),
    path('crud', crud_view, name='crud'),





    ]