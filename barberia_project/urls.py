from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from citas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Autenticación
    path('', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    
    # Home
    path('home/', views.home, name='home'),
    
    # Clientes
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', views.cliente_delete, name='cliente_delete'),
    
    # Barberos
    path('barberos/', views.barbero_list, name='barbero_list'),
    path('barberos/crear/', views.barbero_create, name='barbero_create'),
    path('barberos/<int:pk>/editar/', views.barbero_update, name='barbero_update'),
    path('barberos/<int:pk>/eliminar/', views.barbero_delete, name='barbero_delete'),
    
    # Servicios
    path('servicios/', views.servicio_list, name='servicio_list'),
    path('servicios/crear/', views.servicio_create, name='servicio_create'),
    path('servicios/<int:pk>/editar/', views.servicio_update, name='servicio_update'),
    path('servicios/<int:pk>/eliminar/', views.servicio_delete, name='servicio_delete'),
    
    # Citas
    path('citas/', views.cita_list, name='cita_list'),
    path('citas/crear/', views.cita_create, name='cita_create'),
    path('citas/<int:pk>/editar/', views.cita_update, name='cita_update'),
    path('citas/<int:pk>/eliminar/', views.cita_delete, name='cita_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)