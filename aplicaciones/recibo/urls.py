from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('formularioClientes/', views.formularioClientes, name='formularioClientes'),
    path('editarCliente/', views.editarCliente),
    path('edicionCliente/<codigo>', views.edicionCliente),
    path('eliminarCliente/<codigo>', views.eliminarCliente),
    path('registro/', views.registro),
    path('buscar-cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('recibo/', views.buscar_cliente, name='recibo'),
    path('print/', views.print_view, name='print')
]