from django.shortcuts import render, get_object_or_404, redirect

from galeria.models import Fotografia

# Importando usuarios do Django:
from django.contrib.auth.models import User

# Importar biblioteca de autenticação:
from django.contrib import auth

# Importa biblioteca de Alertas e mensagens do django:
from django.contrib import messages


def index(request):
    # Validação de entrada de usuario:
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    # Listando todas as fotografias
    # fotografias = Fotografia.objects.all()
    # Filtrando as publicadas, adicionando o '-' na frente do campo pega do mais antigo
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    # Validação de entrada de usuario:
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    # Faz um select geral das fotografias
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    # Faz um filtro dentro das informações dentro da URL
    if "buscar" in request.GET:
        # Faz referencia ao input chamado 'buscar' do html o index
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            # Filtra dentro do nome se contem a palavra 'VARIAVEL__icontains'
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, "galeria/buscar.html", {"cards": fotografias})