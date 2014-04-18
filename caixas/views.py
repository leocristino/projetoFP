# This Python file uses the following encoding: utf-8
# ANOTAÇÃO PARA USAR CARACTERES ESPECIAIS AQUI. (MESMO PARA ANOTAÇÕES.)
""" 
@edsonlb
https://www.facebook.com/groups/pythonmania/
"""

from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q #Queries complexas
from caixas.models import Conta

def index(request):
    return render(request, 'index.html')

def caixaListar(request):
    caixas = Conta.objects.all()[0:10]

    return render(request, 'caixas/listaCaixas.html', {'caixas': caixas})


def caixaAdicionar(request):
    return render(request, 'caixas/formCaixas.html')

def caixaSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')

        try:
            caixa = Conta.objects.get(pk=codigo)
        except:
            caixa = Conta()

        caixa.pessoa_id = request.POST.get('pessoa_id', '')
        caixa.tipo = request.POST.get('tipo', '').upper()
        caixa.descricao = request.POST.get('descricao', '').upper()
        caixa.valor = request.POST.get('valor', '')
        caixa.pagseguro = request.POST.get('pagseguro', '')

        caixa.save()
    return HttpResponseRedirect('/caixas/')

def caixaPesquisar(request):
    if request.method == 'POST':
        textoBusca = request.POST.get('textoBusca', 'TUDO').upper()

        try:
            if textoBusca == 'TUDO':
                caixas = Conta.objects.all()
            else: 
                caixas = Conta.objects.filter(
                    (Q(tipo__contains=textoBusca) |  
                    Q(descricao__contains=textoBusca) | 
                    Q(valor__contains=textoBusca) | 
                    Q(pagseguro__contains=textoBusca)))
                    
        except:
            caixas = []

        return render(request, 'caixas/listaCaixas.html', {'caixas': caixas, 'textoBusca': textoBusca})

def caixaEditar(request, pk=0):
    try:
        caixa = Conta.objects.get(pk=pk)
    except:
        return HttpResponseRedirect('/caixas/')

    return render(request, 'caixas/formCaixas.html', {'caixa': caixa})

def caixaExcluir(request, pk=0):
    try:
        caixa = Conta.objects.get(pk=pk)
        caixa.delete()
        return HttpResponseRedirect('/caixas/')
    except:
        return HttpResponseRedirect('/caixas/')




    




