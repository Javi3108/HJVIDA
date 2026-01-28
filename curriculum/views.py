import os
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings

# Importación de tus modelos
from .models import (
    DatosPersonales, 
    ExperienciaLaboral, 
    EstudioRealizado, 
    CursoCapacitacion, 
    Reconocimiento, 
    ProductoAcademico, 
    VentaGarage
)

def inicio(request):
    """Vista para la página de inicio."""
    perfil = DatosPersonales.objects.first()
    return render(request, 'curriculum/inicio.html', {'perfil': perfil})

def perfil(request):
    """Vista para los datos personales."""
    perfil_data = DatosPersonales.objects.first()
    return render(request, 'curriculum/datos_personales.html', {'perfil': perfil_data})

def experiencia(request):
    """Vista para la trayectoria profesional."""
    experiencias = ExperienciaLaboral.objects.filter(activo=True).order_by('-fecha_inicio')
    return render(request, 'curriculum/experiencia.html', {'experiencias': experiencias})

def educacion(request):
    """Vista para formación académica."""
    estudios = EstudioRealizado.objects.filter(activo=True).order_by('-fecha_fin')
    return render(request, 'curriculum/educacion.html', {'estudios': estudios})

def cursos(request):
    """Vista para cursos y certificaciones."""
    cursos_list = CursoCapacitacion.objects.filter(activo=True).order_by('-fecha_realizacion')
    return render(request, 'curriculum/cursos.html', {'cursos': cursos_list})

def reconocimientos(request):
    """Vista para premios y reconocimientos."""
    logros = Reconocimiento.objects.filter(activo=True).order_by('-fecha_obtencion')
    return render(request, 'curriculum/reconocimientos.html', {'reconocimientos': logros})

def trabajos(request):
    """Vista para productos académicos/proyectos."""
    proyectos = ProductoAcademico.objects.filter(activo=True).order_by('-fecha_publicacion')
    return render(request, 'curriculum/proyectos.html', {'trabajos': proyectos})

def venta(request):
    """Vista para el Marketplace/Venta de Garage."""
    productos = VentaGarage.objects.filter(activo=True)
    perfil = DatosPersonales.objects.first()
    return render(request, 'curriculum/venta.html', {'productos': productos, 'perfil': perfil})

def contacto(request):
    """Vista para información de contacto."""
    perfil = DatosPersonales.objects.first()
    return render(request, 'curriculum/contacto.html', {'perfil': perfil})

def seleccionar_cv(request):
    """Vista para la interfaz de selección de secciones para el PDF."""
    return render(request, 'curriculum/seleccionar_pdf.html')

def generar_cv(request):
    """Genera el PDF dinámico con todas las secciones corregidas."""
    perfil = DatosPersonales.objects.first()
    
    # Captura de checkboxes desde el formulario (seleccionar_pdf.html)
    ver_exp = request.GET.get('ver_experiencia') == 'on'
    ver_edu = request.GET.get('ver_educacion') == 'on'
    ver_cur = request.GET.get('ver_cursos') == 'on'
    ver_log = request.GET.get('ver_logros') == 'on'
    ver_pro = request.GET.get('ver_proyectos') == 'on'

    # Preparar el contexto sincronizado con la plantilla cv_pdf.html
    context = {
        'perfil': perfil,
        'experiencias': ExperienciaLaboral.objects.filter(activo=True).order_by('-fecha_inicio') if ver_exp else [],
        'estudios': EstudioRealizado.objects.filter(activo=True).order_by('-fecha_fin') if ver_edu else [],
        'cursos': CursoCapacitacion.objects.filter(activo=True).order_by('-fecha_realizacion') if ver_cur else [],
        'logros': Reconocimiento.objects.filter(activo=True).order_by('-fecha_obtencion') if ver_log else [],
        'proyectos': ProductoAcademico.objects.filter(activo=True).order_by('-fecha_publicacion') if ver_pro else [],
    }

    # Crear la respuesta PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="CV_Profesional.pdf"'
    
    # Cargar y renderizar la plantilla
    template = get_template('curriculum/cv_pdf.html')
    html = template.render(context)
    
    # Crear el PDF usando pisa
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error técnico al generar el archivo PDF', status=500)
        
    return response