from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormServico
from django.http import HttpResponse, FileResponse
from .models import Servico
from fpdf import FPDF
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

    

@login_required(login_url="/usuarios/login/")
def novo_servico(request):
    if request.method == "GET":
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/servicos/listar_servico/')
        else:
            return render(request, 'novo_servico.html', {'form': form})

@login_required(login_url="/usuarios/login/")
def listar_servico(request):
    if request.method == "GET":
        servicos = Servico.objects.all()
        return render(request, 'listar_servico.html', {'servicos': servicos})
    
    
@login_required(login_url="/usuarios/login/")
def servico(request, servico_id):
    servico = Servico.objects.get(id=servico_id)
    categorias = servico.categoria_manutencao.all()

    return render(request, 'servico.html', {'servico': servico, 'categorias': categorias})

def finalizar_servico(request, servico_id):
    try:
        servico = Servico.objects.get(id=servico_id)
        servico.finalizado = True
        servico.save()
        return JsonResponse({'status': 'success', 'finalizado': servico.finalizado})
    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Servico não encontrado'})

