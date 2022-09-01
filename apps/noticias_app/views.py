from multiprocessing import context
from time import timezone
from django.shortcuts import render, redirect
from .models import Evento, Noticia,Comentarios,Categoria
from django.http.response import Http404
from django.conf import settings
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ComentarioForm, NoticiaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( CreateView)


# Create your views here.

def base(request):
    return render(request, 'base.html', {})

def index(request):
    return render(request, 'index.html', {})

def noticias(request):
    lista_de_noticias = Noticia.objects.all().order_by('creado').reverse()
    lista_de_categorias = Categoria.objects.all()
    context = {
        "noticias" : lista_de_noticias,
        "categorias" : lista_de_categorias,
    }
    return render(request, '/noticias/noticias.html', context)

def eventos(request):
    lista_de_eventos = Evento.objects.all().order_by('creado').reverse()
    lista_de_categorias = Categoria.objects.all()

    context = {
        "eventos" : lista_de_eventos,
        "categorias" : lista_de_categorias,
    }
    return render(request, 'eventos.html', context)



def nosotros(request):
    return render(request, 'nosotros.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def noticiadetalle(request,id):
    try:
        datanoticia = Noticia.objects.get(id=id)
        lista_comentarios = Comentarios.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La noticia solicitada no existe.')

    form = ComentarioForm()
    
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comment = Comentarios(
                autor_id = request.user.id,
                cuerpo_comentario=form.cleaned_data["cuerpo_comentario"],
                noticia=datanoticia
            )
            comment.save()

    context = {
        "noticia": datanoticia,
        "comentarios":lista_comentarios,
        "MEDIA_ROOT": 'static/img/noticias/',
        "form" : ComentarioForm(),
    }

    return render(request, 'noticias-detalle.html', context)

class CrearNoticiaView(CreateView, LoginRequiredMixin):
    login_url = '/login'

    form_class = NoticiaForm
    model = Noticia

def categoriaNoticia(request, id):

    try:
        lista_categorias = Categoria.objects.all()
        categoria = Categoria.objects.get(id = id)
        noticias = Noticia.objects.filter(categorias = id)
        lista_comentarios = Comentarios.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')\
    
    form = ComentarioForm()
    
    if (request.method == "POST") and (request.user.id != None):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comment = Comentarios(
                autor_id = request.user.id,
                cuerpo_comentario=form.cleaned_data["cuerpo_comentario"],
                noticia=noticias
            )
            comment.save()
            return redirect("Noticia")

    context = {
        "categori":categoria,
        "categorias":lista_categorias,
        "form":form,
        "noticias": noticias,
        "comentarios": lista_comentarios
    }
    return render(request, 'noticias.html', context)

@login_required
def comment_approve(request, id):
    try:
        comentarios = Comentarios.objects.get(id=id)
    except:
        raise Http404("El comentario no existe")

    comentarios.approve()
    return redirect('noticiadetalle', id=comentarios.noticia.id)

@login_required
def comment_remove(request, id):
    try:
        comentarios = Comentarios.objects.get(id=id)
    except:
        raise Http404("El comentario no existe")

    comentarios.delete()
    return redirect('noticiadetalle', id=comentarios.noticia.id)