from django.shortcuts import render , redirect
from perfil.models import Conta , Categoria
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse



def definir_planejamento(request):
    categorias = Categoria.objects.all()
    # messages.add_message(request,     constants.SUCCESS, 'Valor alterado.')

    return render(request, 'definir_planejamento.html', {'categorias': categorias , 'messages':messages.get_messages(request)} )

@csrf_exempt
def update_valor_categoria(request , id_c):
    print("id " + str(id_c))
    valor = json.load(request)['valor']
    messages.add_message(request, constants.SUCCESS, 'Valor alterado.')
    valor_f = -1
    if(valor):
        try:
            valor = float(valor)
            if(valor > 0):
                categoria = Categoria.objects.get(id = id_c)
                print(valor)
                categoria.valor_planejamento = valor
                valor_f  = categoria.valor_planejamento
                print(categoria.valor_planejamento)
                categoria.save()
                messages.add_message(request, constants.SUCCESS, 'Valor alterado.')
            else:
                
                print("valor negativo")
                raise ValueError("Valor < 0 inválido")

        except ValueError:
            print("valor negativo except")
            messages.add_message(request, constants.ERROR, 'Adicione um valor maior que zero!')

    else:
        messages.add_message(request, constants.ERROR, 'O campo não pode estar vazio!')
    redirect('/planejamento/definir_planejamento' )
    return HttpResponse({'valorFinal':valor_f})

def ver_planejamento(request):
    categorias = Categoria.objects.all()
        
    return render(request, 'ver_planejamento.html', {'categorias': categorias})
