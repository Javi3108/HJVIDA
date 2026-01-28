from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.inicio, name='inicio'),
    
    # Secciones del CV
    path('perfil/', views.perfil, name='perfil'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('educacion/', views.educacion, name='educacion'),
    path('cursos/', views.cursos, name='cursos'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    
    # Otras secciones
    path('trabajos/', views.trabajos, name='trabajos'),
    path('venta/', views.venta, name='venta'),
    path('contacto/', views.contacto, name='contacto'),
    
    # Rutas para el PDF
    path('seleccionar-cv/', views.seleccionar_cv, name='seleccionar_cv'),
    path('generar-cv/', views.generar_cv, name='generar_cv'), # Este es el que usa el botón
]