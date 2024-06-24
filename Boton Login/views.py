from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, render
from django.contrib import messages

def logeo(request):
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']
        contraseña = request.POST['contraseña']
        usuario = request.POST['usuario']
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectas')
    return render(request, 'logeo.html')