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


