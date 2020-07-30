from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from profiles.forms import FormularioRegistro
from django.contrib.auth.models import User

User = get_user_model()


def registro(request):
    """
    View para registro de usuarios. Cuando un usuario se registra, se realiza
    el login automáticamente.
    """
    if request.method == "POST":
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            messages.success(
                request, 'Registro realizado correctamente y usuario logado.'
            )

            return redirect('dashboard')

        return render(request, 'dashboard.html')

    else:
        form = FormularioRegistro()
        context = {'form': form}
        return render(request, 'registro.html', context)


def loginv(request):
    """
    View con la lógica de login de usuarios.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login realizado correctamente.")
                print("Login realizado correctamente.")
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
                print("Usuario o contraseña incorrectos.")
                return redirect('loginv')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            print("Usuario o contraseña incorrectos.")
            return redirect('loginv')

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def logoutv(request):
    """
    View con la lógica de logout de usuarios.
    """
    logout(request)
    messages.success(request, 'Logout exitoso.')
    return redirect('index')
