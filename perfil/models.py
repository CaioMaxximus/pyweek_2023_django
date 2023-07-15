from django.db import models
from datetime import datetime
# Create your models here.

class Categoria(models.Model):
    
    categoria = models.CharField(max_length= 45)
    essencial = models.BooleanField(default= False)
    valor_planejamento = models.FloatField(default = 0)
    
    
    def computa_valor_gasto(self):
        from extrato.models import Valores
        valores = Valores.objects.filter(categoria__id= self.id).filter(data__month = datetime.now().month).filter(tipo = 'S')
        sum_valores = 0
        for extrato in valores:
            sum_valores += extrato.valor
        print(sum_valores)
        return sum_valores
    
    def computa_fracao_gasto(self):
        valor_gasto = self.computa_valor_gasto()
        if(valor_gasto > 0):
            saida = int(self.computa_valor_gasto() / self.valor_planejamento * 100)
            print("saida" + str(saida))
            return str(saida)
        else:
            return 0
    def __str__(self):
        return self.categoria 
    
class Conta(models.Model):
    banco_choices = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa econômica'),
    )

    tipo_choices = (
        ('pf', 'Pessoa física'),
        ('pj', 'Pessoa jurídica'),
    )

    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=banco_choices)
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to='icones')

    def __str__(self):
        return self.apelido