from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Cliente, Barbero, Servicio, Cita, Horario
from django.db.models import Q


# ==================== AUTENTICACIÓN ====================

def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            try:
                from django.contrib.auth.models import User
                user = User.objects.create_user(username=username, password=password1)
                messages.success(request, '¡Registro exitoso! Por favor inicia sesión.')
                return redirect('login')
            except:
                messages.error(request, 'El nombre de usuario ya existe.')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
    
    return render(request, 'registro.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido, {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')


@login_required
def home(request):
    context = {
        'total_clientes': Cliente.objects.count(),
        'total_barberos': Barbero.objects.count(),
        'total_servicios': Servicio.objects.count(),
        'total_citas': Cita.objects.count(),
        'citas_pendientes': Cita.objects.filter(estado='Pendiente').count(),
    }
    return render(request, 'home.html', context)


# ==================== CRUD CLIENTES ====================

@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    query = request.GET.get('q')
    if query:
        clientes = clientes.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) |
            Q(telefono__icontains=query)
        )
    return render(request, 'cliente_list.html', {'clientes': clientes})


@login_required
def cliente_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        
        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            correo=correo
        )
        messages.success(request, 'Cliente creado exitosamente.')
        return redirect('cliente_list')
    
    return render(request, 'cliente_form.html')


@login_required
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.telefono = request.POST.get('telefono')
        cliente.correo = request.POST.get('correo')
        cliente.save()
        
        messages.success(request, 'Cliente actualizado exitosamente.')
        return redirect('cliente_list')
    
    return render(request, 'cliente_form.html', {'cliente': cliente})


@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente.')
        return redirect('cliente_list')
    
    return render(request, 'cliente_confirm_delete.html', {'cliente': cliente})


# ==================== CRUD BARBEROS ====================

@login_required
def barbero_list(request):
    barberos = Barbero.objects.all()
    query = request.GET.get('q')
    if query:
        barberos = barberos.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) |
            Q(especialidad__icontains=query)
        )
    return render(request, 'barbero_list.html', {'barberos': barberos})


@login_required
def barbero_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        especialidad = request.POST.get('especialidad')
        
        Barbero.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            especialidad=especialidad
        )
        messages.success(request, 'Barbero creado exitosamente.')
        return redirect('barbero_list')
    
    return render(request, 'barbero_form.html')


@login_required
def barbero_update(request, pk):
    barbero = get_object_or_404(Barbero, pk=pk)
    
    if request.method == 'POST':
        barbero.nombre = request.POST.get('nombre')
        barbero.apellido = request.POST.get('apellido')
        barbero.telefono = request.POST.get('telefono')
        barbero.especialidad = request.POST.get('especialidad')
        barbero.save()
        
        messages.success(request, 'Barbero actualizado exitosamente.')
        return redirect('barbero_list')
    
    return render(request, 'barbero_form.html', {'barbero': barbero})


@login_required
def barbero_delete(request, pk):
    barbero = get_object_or_404(Barbero, pk=pk)
    
    if request.method == 'POST':
        barbero.delete()
        messages.success(request, 'Barbero eliminado exitosamente.')
        return redirect('barbero_list')
    
    return render(request, 'barbero_confirm_delete.html', {'barbero': barbero})


# ==================== CRUD SERVICIOS ====================

@login_required
def servicio_list(request):
    servicios = Servicio.objects.all()
    query = request.GET.get('q')
    if query:
        servicios = servicios.filter(
            Q(nombre__icontains=query) | 
            Q(descripcion__icontains=query)
        )
    return render(request, 'servicio_list.html', {'servicios': servicios})


@login_required
def servicio_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        duracion = request.POST.get('duracion')
        
        Servicio.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            duracion=duracion
        )
        messages.success(request, 'Servicio creado exitosamente.')
        return redirect('servicio_list')
    
    return render(request, 'servicio_form.html')


@login_required
def servicio_update(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    
    if request.method == 'POST':
        servicio.nombre = request.POST.get('nombre')
        servicio.descripcion = request.POST.get('descripcion')
        servicio.precio = request.POST.get('precio')
        servicio.duracion = request.POST.get('duracion')
        servicio.save()
        
        messages.success(request, 'Servicio actualizado exitosamente.')
        return redirect('servicio_list')
    
    return render(request, 'servicio_form.html', {'servicio': servicio})


@login_required
def servicio_delete(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    
    if request.method == 'POST':
        servicio.delete()
        messages.success(request, 'Servicio eliminado exitosamente.')
        return redirect('servicio_list')
    
    return render(request, 'servicio_confirm_delete.html', {'servicio': servicio})


# ==================== CRUD CITAS ====================

@login_required
def cita_list(request):
    citas = Cita.objects.select_related('cliente', 'barbero', 'servicio').all()
    query = request.GET.get('q')
    if query:
        citas = citas.filter(
            Q(cliente__nombre__icontains=query) | 
            Q(cliente__apellido__icontains=query) |
            Q(fecha__icontains=query)
        )
    return render(request, 'cita_list.html', {'citas': citas})


@login_required
def cita_create(request):
    clientes = Cliente.objects.all()
    barberos = Barbero.objects.all()
    servicios = Servicio.objects.all()
    
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        barbero_id = request.POST.get('barbero')
        servicio_id = request.POST.get('servicio')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        estado = request.POST.get('estado', 'Pendiente')
        observaciones = request.POST.get('observaciones')
        
        Cita.objects.create(
            cliente_id=cliente_id,
            barbero_id=barbero_id,
            servicio_id=servicio_id,
            fecha=fecha,
            hora=hora,
            estado=estado,
            observaciones=observaciones
        )
        messages.success(request, 'Cita creada exitosamente.')
        return redirect('cita_list')
    
    return render(request, 'cita_form.html', {
        'clientes': clientes,
        'barberos': barberos,
        'servicios': servicios
    })


@login_required
def cita_update(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    clientes = Cliente.objects.all()
    barberos = Barbero.objects.all()
    servicios = Servicio.objects.all()
    
    if request.method == 'POST':
        cita.cliente_id = request.POST.get('cliente')
        cita.barbero_id = request.POST.get('barbero')
        cita.servicio_id = request.POST.get('servicio')
        cita.fecha = request.POST.get('fecha')
        cita.hora = request.POST.get('hora')
        cita.estado = request.POST.get('estado')
        cita.observaciones = request.POST.get('observaciones')
        cita.save()
        
        messages.success(request, 'Cita actualizada exitosamente.')
        return redirect('cita_list')
    
    return render(request, 'cita_form.html', {
        'cita': cita,
        'clientes': clientes,
        'barberos': barberos,
        'servicios': servicios
    })


@login_required
def cita_delete(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    
    if request.method == 'POST':
        cita.delete()
        messages.success(request, 'Cita eliminada exitosamente.')
        return redirect('cita_list')
    
    return render(request, 'cita_confirm_delete.html', {'cita': cita})