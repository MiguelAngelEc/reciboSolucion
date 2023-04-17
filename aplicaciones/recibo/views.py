from django.shortcuts import render, redirect
from .models import cliente
from django.contrib import messages

# Create your views here.
def home(request):
       clientesListados = cliente.objects.all()
       # Despliega informacion a la pagina principal
       return render(request, "gestionLista.html", {"listado": clientesListados})

def formularioClientes(request):
    # código de tu vista aquí
    return render(request, 'formularioClientes.html')

def recibo(request):
    # código de tu vista aquí
    return render(request, 'recibo.html')

def registro(request):
    if request.method == 'POST':
        codigo = request.POST.get('txtCodigo')
        nombre = request.POST.get('txtnombre')
        direccion = request.POST.get('txtdireccion')
        ciudad = request.POST.get('txtciudad')
        telefono = request.POST.get('txttelefono')
        email = request.POST.get('txtcorreo')
        
        # Comprueba si ya existe un registro con el mismo código
        if cliente.objects.filter(codigo=codigo).exists():
            messages.warning(request, 'Ya existe un cliente con ese código')
        else:
            # Crea el registro en la base de datos
            listado = cliente.objects.create(codigo=codigo, Nombre_Apellido=nombre, Direccion=direccion, Ciudad=ciudad, Telefono=telefono, email=email)
            messages.success(request, 'Cliente Ingresado!!')
            
        return redirect('/')
    
    # Si no se ha enviado un formulario, renderiza la plantilla del formulario
    return render(request, 'registro.html')

#Codigo para edicion
def edicionCliente(request, codigo):
       listado = cliente.objects.get(codigo=codigo)
       return render(request, "edicionCliente.html", {"listado": listado})

def editarCliente(request):
       codigo=request.POST['txtCodigo']
       nombre=request.POST['txtNombreApellido']
       direccion=request.POST['txtDireccion']
       ciudad=request.POST['txtCiudad']
       telefono=request.POST['txtTelefono']
       email=request.POST['txtEmail']
       
       listado = cliente.objects.get(codigo=codigo)
       listado.Nombre_Apellido = nombre
       listado.Direccion = direccion
       listado.Ciudad = ciudad
       listado.Telefono = telefono
       listado.email = email
       listado.save()
       
       return redirect('/')

#Codigo para eliminar
def eliminarCliente(request, codigo):
       listado = cliente.objects.get(codigo=codigo)
       listado.delete()
       messages.success(request, 'Cliente Eliminado!!')
       return redirect('/')

# Codigo para Buscar Cliente
def buscar_cliente(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        cliente.objects.filter(codigo=codigo).first()
        if cliente:
            return render(request, 'reciboCliente.html', {'cliente': cliente})
        else:
            mensaje = f"No se encontró un cliente con el código {codigo}."
            return render(request, 'reciboCliente.html', {'mensaje': mensaje})
    else:
        return render(request, 'reciboCliente.html')