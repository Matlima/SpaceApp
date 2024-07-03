from django.shortcuts import render

dados = {
    1: {"nome": "Nebulosa de Carina",
        "legenda": "webbtelecope.org / NASA / James Webb"},
    2: { "nome": "Galáxia NGC 1079",
        "legenda": "nasa.org / NASA / Hubble"}
}

def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webbtelecope.org / NASA / James Webb"},
        2: { "nome": "Galáxia NGC 1079",
            "legenda": "nasa.org / NASA / Hubble"}
    }
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html' )


