from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('perfil/', views.perfil, name='perfil'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('educacion/', views.educacion, name='educacion'),
    path('cursos/', views.cursos, name='cursos'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('trabajos/', views.trabajos, name='trabajos'),
    path('venta/', views.venta, name='venta'),
    path('contacto/', views.contacto, name='contacto'),
    # Ruta para la pantalla de selección
    path('seleccionar-cv/', views.seleccionar_cv, name='seleccionar_cv'),
    # Tu ruta de generación (se mantiene igual)
    path('generar-cv/', views.generar_cv, name='generar_cv'),
]