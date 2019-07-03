from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor

# Create your views here.
def Home(request):
    return render(request, 'index.html')


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        print(autor_form)

        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')

    else:
        autor_form = AutorForm()
        print(autor_form)
    return render(request, 'libro/crear_autor.html', {'autor_form':autor_form})

def listarAutor(request):
    autores = Autor.objects.filter(estado = True)
    return render(request, 'libro/listar_autores.html', {'autores':autores})


def editarAutor(request, id):
    error = None
    autor_form = None
    try:
        autor = Autor.objects.get(id = id)
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'libro/crear_autor.html', {'autor_form':autor_form, 'error':error})


def eliminarAutor(request, id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autores')
    return render(request, 'libro/eliminar_autor.html', {'autor':autor})
