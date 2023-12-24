from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe usuario nome')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return redirect('/usuarios/login/')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username=username, email=email, password=senha)

        if user:
            login_django(request, user)
            return redirect('/clientes')
        else:
            return HttpResponse("Dados invalidos")

@login_required(login_url="/usuarios/login/")
def plataforma(request):
    return HttpResponse("Plataforma")
