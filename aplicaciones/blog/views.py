from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Post,Categoria,Autor
from django.shortcuts import get_object_or_404
from .forms import AutorForm
from django.views.generic import View

"""
    1.- dispatch(): valida la peticion y elige que metodo HTTP se utilozo para la solicitud
    2.- http_method_not_allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
    3.- options()
"""


class Index(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')


def administrador(request):
    return render(request,'administrador.html')

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def detallePost(request,slug):
    post = get_object_or_404(Post,slug = slug)
    return render(request,'post.html',{'detalle_post':post})

def generales(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Generales')
    )
    return render(request,'generales.html',{'posts':posts})

def aplicacion(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Aplicacion')
    )
    return render(request,'aplicacion.html',{'posts':posts})

def tutoriales(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
    )
    return render(request,'tutoriales.html',{'posts':posts})


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
        return redirect('blog:listar_autor')
    else:
        autor_form = AutorForm()
    return render(request,'crear_autor.html',{'autor_form':autor_form})

def listarAutor(request):
    autores = Autor.objects.filter(estado = True)
    return render(request,'listar_autor.html',{'autores':autores})

def editarAutor(request,id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id = id)

        if request.method == 'GET':
            autor_form = AutorForm(instance = autor)
        else:
            autor_form = AutorForm(request.POST, instance = autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('blog:listar_autor')
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'crear_autor.html',{'autor_form':autor_form,'error':error})

def eliminarAutor(request,id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        #hotel.delete()
        return redirect('blog:listar_autor')
    return render(request,'eliminar_autor.html',{'autor':autor})
