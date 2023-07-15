from django.shortcuts import render , redirect ,HttpResponse
from perfil.models import Categoria , Conta
from .models import Valores
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime

def novo_valor(request):
    if request.method == "GET":
        contas = Conta.objects.all()
        categorias = Categoria.objects.all() 
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    else :
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo')
        
        valores = Valores(
            valor=valor,
            categoria_id=categoria,
            descricao=descricao,
            data=data,
            conta_id=conta,
            tipo=tipo,
        )

        valores.save()
        conta = Conta.objects.get(id=conta)

        if tipo == 'E':
            conta.valor += int(valor)
        else:
            conta.valor -= int(valor)

        conta.save()
        messages.add_message(request, constants.SUCCESS, 'Novo valor com sucesso')
        return redirect('/extrato/novo_valor')

def view_extrato(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()    
    valores = Valores.objects.filter(data__month=datetime.now().month)
    
    filtro_catg = request.GET.get('categoria')
    filtro_conta = request.GET.get('conta')
    
    if(filtro_catg):
        valores = valores.filter(categoria__id=filtro_catg)
        
    if(filtro_conta):
        valores = valores.filter(conta__id=filtro_conta)
        
    #TODO: FILTRAR PELO PERÍODO DE TEMPO

    return render(request, 'view_extrato.html', {'valores': valores, 'contas': contas, 'categorias': categorias})

def exportar_pdf(request):
    
    return HttpResponse("a implementar")