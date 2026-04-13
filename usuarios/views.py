from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'usuarios/login.html', {'erro': 'Usuário inválido'})

    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('/usuarios/login/')