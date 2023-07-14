from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lanzamientos/', views.lanzamientos, name='lanzamientos'),
    path('sobre-mi/', views.sobremi, name='sobremi'),
    path('no-disponible/', views.nada, name='nada'),
    path('segunda-vista/', views.segunda_vista, name='segunda_vista'),
    path('fecha-actual/', views.fecha_actual, name='fecha_actual'),
    path('saludar/', views.saludar, name='saludar'),
    path('saludar/<str:nombre>/<str:apellido>/', views.bienvenida, name='bienvenida'),
    
    # CBV
    path('sugerencias/', views.ListarSugerencias.as_view(), name='listar_sugerencias'),
    path('sugerencias/crear/', views.CrearSugerencia.as_view(), name='crear_sugerencia'),
    path('sugerencias/eliminar/<int:pk>/', views.EliminarSugerencia.as_view(), name='eliminar_sugerencia'),
    path('sugerencias/modificar/<int:pk>/', views.ModificarSugerencia.as_view(), name='modificar_sugerencia'),
    path('sugerencias/<int:pk>/', views.MostrarSugerencia.as_view(), name='mostrar_sugerencia'),
]