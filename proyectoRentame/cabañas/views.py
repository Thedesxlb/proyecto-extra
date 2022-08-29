from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from cabañas.forms import CabañasForm, ContactoForm
from .models import Cabañas, Promociones, Opinion
from django.contrib import messages 

# Create your views here.

def catalogo(request):
    catalogo = Cabañas.objects.all()
    return render(request, "cabañas/catalogo.html", {'catalogo':catalogo})

def promociones(request):
    promociones = Promociones.objects.all()
    return render(request, "cabañas/promociones.html", {'promociones':promociones})


def opiniones(request):
    dudas = Opinion.objects.all()
    return render(request, "cabañas/opiniones.html", {'dudas':dudas})


# def registrarOpinion(request):
#     if request.method == 'POST':
#         form = ContactoForm(request.POST,)
#         if form.is_valid(): #Si los datos recibidos son correctos
#             form.save() #inserta
#             dudas = Opinion.objects.all()
#             return render(request,'cabañas/opiniones.html', {'dudas': dudas})
#     form = ContactoForm()
#     #Si algo sale mal se reenvian al formulario los datos ingresados
#     return render(request,'cabañas/Registraropiniones.html',{'form': form})

def registrarOpinion(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST, request.FILES)
        if form.is_valid():
            nombreClien =request.POST['nombreClien']
            nombreCabaña =request.POST['nombreCabaña']
            duda =request.POST['duda']
            imagenOp =request.FILES['imagenOp']
            insert = Opinion(nombreClien=nombreClien, nombreCabaña=nombreCabaña, duda=duda, imagenOp=imagenOp)
            insert.save()
            return render(request, "cabañas/opiniones.html")
        else:
            messages.error(request, 'Error al subir el archivo')
    else:
        return render(request, 'cabañas/Registraropiniones.html', {'Opinion':Opinion})




def consultarDuda(request, id):
    duda = Opinion.objects.get(id=id)
    return render(request, 'cabañas/editarOpinion.html', {'duda': duda})

def editarDuda(request, id):
    duda = get_object_or_404(Opinion, id=id)
    form = CabañasForm(request.POST, instance=duda)
    if form.is_valid():
            form.save()
            dudas = Opinion.objects.all()
            return render(request, 'cabañas/opiniones.html', {'dudas': dudas})
    return render(request, 'cabañas/editarOpinion.html', {'form':form})


def eliminarDuda(request, id, 
    confirmacion = 'cabañas/confirmarEliminacion.html'):
    duda = get_object_or_404(Opinion, id=id)
    if request.method == 'POST':
        duda.delete()
        dudas = Opinion.objects.all()
        return render(request, 'cabañas/opiniones.html', {'dudas': dudas})
    return render(request, confirmacion, {'object': duda})