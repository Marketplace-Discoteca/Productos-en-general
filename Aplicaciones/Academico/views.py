from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages

def home(request):
    productosListados = Producto.objects.all()
    messages.success(request, '¡Productos listados!')
    return render(request, "gestionProductos.html", {"productos": productosListados})

def registrarProducto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    return render(request, 'registroProducto.html', {'form': form})

def edicionProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Producto actualizado!')
            return redirect('detalleProducto', id=producto.id)  # Redirigir a la vista de detalles del producto
    else:
        form = ProductoForm(instance=producto)
        
    return render(request, "edicionProducto.html", {'form': form, 'producto': producto})


def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, '¡Producto eliminado!')
    return redirect('home')

def detalleProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, "detalleProducto.html", {'producto': producto})
