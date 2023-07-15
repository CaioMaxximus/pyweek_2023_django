from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Conta , Categoria
from extrato.models import Valores
# Create your views here.
from .util import calcula_total 
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from datetime import datetime


def home(request):
    contas = Conta.objects.all()
    total = calcula_total(contas , 'valor')
    valores = Valores.objects.filter(data__month = datetime.now().month)
    valores_e  = calcula_total(valores.filter(tipo = 'E'), 'valor') 
    valores_s = calcula_total(valores.filter(tipo = 'S'), 'valor')
    
    essencial = 0
    n_essencial = 0
    
    for valor in valores.filter(tipo = 'S'):
        categoria = Categoria.objects.get(id = valor.categoria_id)
        print(categoria.essencial)
        if(categoria.essencial):
            essencial += valor.valor
        else:
            n_essencial += valor.valor

    essencial_p = 0
    n_essencial_p = 0

    try :
        essencial_p = int(essencial / (essencial + n_essencial) * 100)
        n_essencial_p = int(n_essencial / (essencial + n_essencial) * 100) 
    except:
       print("divisao por zero")
    
    
      
    return render(request,'home.html', {'contas': contas , 'valor_total' : total, 
                                        'valores_e': valores_e , 'valores_s' : valores_s,
                                        'essencial_p' : essencial_p , 'n_essencial_p' : n_essencial_p})

def gerenciar(request):
    contas = Conta.objects.all()
    total = calcula_total(contas , 'valor')
    categorias = Categoria.objects.all()
    return render(request , 'gerenciar.html',{'contas': contas, 'total' : total , 'categorias' : categorias} ) 

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request , constants.WARNING, "Preencha os dados por completo!")
        return redirect('/perfil/gerenciar')
    if (icone is None ):
        messages.add_message(request, constants.WARNING, "Adicione um ícone")
        return redirect("/perfil/gerenciar")
    
    conta = Conta(
        apelido = apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()
    messages.add_message(request , constants.SUCCESS , "Cadastro realizado com sucesso")
    return redirect('/perfil/gerenciar')

def remover_banco(request,  id):

    conta = Conta.objects.get(id = id)
    conta.delete()
    messages.add_message(request , constants.SUCCESS , "Cadastro removido com sucesso!")
    return redirect('/perfil/gerenciar')

def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    categoria = Categoria(
        categoria=nome,
        essencial=essencial
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso')
    return redirect('/perfil/gerenciar')

def alterar_essencial(request , id):
    
    categoria = Categoria.objects.get(id = id)
    if(categoria.essencial):
        categoria.essencial = False
    else:
        categoria.essencial = True
    
    categoria.save()
    return redirect('/perfil/gerenciar')

def dashboard(request):
    dados = {}
    categorias = Categoria.objects.all()
    for categoria in categorias:
        print(categoria)
        sumV = 0
        valores = Valores.objects.filter(categoria = categoria)
        for valor in valores:
            sumV+= valor.valor
        dados[categoria.categoria] = sumV
    print(list(dados.values()))
    return render(request, 'dashboard.html', {'labels' : list(dados.keys()) , 'values': list(dados.values())})