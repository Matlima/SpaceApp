from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

def index(request):
    # Listando todas as fotografias
    # fotografias = Fotografia.objects.all()
    # --
    # Filtrando as publicadas, adicionando o '-' na frente do campo pega do mais antigo
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
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