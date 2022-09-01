"""ProyectoFinalInfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from apps.noticias_app import views

urlpatterns = [
    path('noticia/<int:id>/', views.noticiadetalle, name='noticiadetalle'),
    # path("noticias/nueva_noticia", views.CrearNoticiaView.as_view(), name='CrearNoticiaView'),
    # path('eventos/<int:id>/', views.eventos, name='eventos'),
    path('comentario/<int:id>/approve', views.comment_approve, name="comment_approve"),
    path('comentario/<int:id>/remove', views.comment_remove, name="comment_remove")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)