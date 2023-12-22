from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Equipe, Mecanico
import re
from django.core import serializers
import json
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required(login_url="/usuarios/login/")
def equipes(request):
    if request.method == "GET":
        equipes_list = Equipe.objects.all()
        return render(request, 'equipes.html', {'equipes': equipes_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        mecanicos = request.POST.getlist('mecanico')
        emails = request.POST.getlist('email')
        cpfs = request.POST.getlist('cpf')

        equipe = Equipe.objects.filter(nome=nome)

        if equipe.exists():
            return render(request, 'equipes.html', {'nome': nome, 'mecanicos': zip(mecanicos, emails, cpfs) })

        equipe = Equipe(
            nome = nome
        )

        equipe.save()

        for mecanico, email, cpf in zip(mecanicos, emails, cpfs):
            mec = Mecanico(mecanico=mecanico, email=email, cpf=cpf, equipe=equipe)
            mec.save()

        return redirect('/equipes')