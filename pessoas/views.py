from django.shortcuts import render, HttpResponseRedirect
from pessoas.models import Pessoa

def index(request):
    return render(request, 'index.html')

def pessoaListar(request):
    #pessoas = Pessoa.objects.all()[0:10]
    pessoas = []
    pessoas.append(Pessoa(nome="Leandro", email="leo_cristino", telefone="99198-5964"))
    pessoas.append(Pessoa(nome="Alex", email="alex-falcucci", telefone="99999-9999"))
    pessoas.append(Pessoa(nome="Leandro", email="leo_cristino", telefone="555555555"))
    pessoas.append(Pessoa(nome="Leandro", email="leo_cristino"))
    return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas})

def pessoaAdicionar(request):
    return render(request, 'pessoas/formPessoas.html')