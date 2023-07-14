from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.views.decorators.http import require_GET
from inicio.models import Sugerencia
from django.shortcuts import render, redirect
from inicio.form import CrearSugerenciaFormulario, BuscarSugerenciaFormulario, ModificarSugerenciaFormulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# v4
@login_required
def lanzamientos(request):
    # template = loader.get_template('inicio.html')
    
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio...',
        'segundos': segundos,
        'segundo_par': segundos%2 == 0,
        'segundo_redondo': segundos%10 == 0,
        'listado_de_numeros': list(range(25))
    }
    # renderizar_template = template.render(diccionario)
    # return HttpResponse(renderizar_template)
    return render(request, 'inicio/lanzamientos.html', diccionario)


@login_required
@require_GET
def sobremi(request):
    # template = loader.get_template('inicio.html')
    
    diccionario = {
    }
    return render(request, 'inicio/sobre_mi.html', diccionario)

@login_required
@require_GET
def nada(request):
    # template = loader.get_template('inicio.html')
    
    diccionario = {
    }
    return render(request, 'inicio/nada.html', diccionario)


    
def inicio(request):
    return render(request, 'inicio/inicio.html')

def segunda_vista(request):
    return HttpResponse('<h1>Soy la segunda vista!</h1>')

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Fecha actual: {fecha}</h1>')

def saludar(request):
    return HttpResponse('Bienvenido/a!!!')

def bienvenida(request, nombre, apellido):
    return HttpResponse(f'Bienvenido/a {nombre.title()} {apellido.title()}!!!')



class CrearSugerencia(CreateView):
    model = Sugerencia
    template_name = 'inicio/CBV/crear_sugerencia_CBV.html'
    fields = ['nombre', 'edad', 'descripcion']
    success_url = reverse_lazy('inicio:listar_sugerencias')
    
class ListarSugerencias(ListView):
    model = Sugerencia
    template_name = "inicio/CBV/listar_sugerencias_CBV.html"
    context_object_name = 'sugerencias'

class ModificarSugerencia(LoginRequiredMixin, UpdateView):
    model = Sugerencia
    template_name = "inicio/CBV/modificar_sugerencia_CBV.html"
    fields = ['nombre', 'edad', 'descripcion']
    success_url = reverse_lazy('inicio:listar_sugerencias')
    
class EliminarSugerencia(LoginRequiredMixin, DeleteView):
    model = Sugerencia
    template_name = "inicio/CBV/eliminar_sugerencia_CBV.html"
    success_url = reverse_lazy('inicio:listar_sugerencias')
    
class MostrarSugerencia(DetailView):
    model = Sugerencia
    template_name = "inicio/CBV/mostrar_sugerencia_CBV.html"
