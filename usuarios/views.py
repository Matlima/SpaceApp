from django.shortcuts import render, redirect

# Importando Formulario:
from usuarios.forms import LoginForms, CadastroForms

# Importando usuarios do Django:
from django.contrib.auth.models import User

# Importar biblioteca de autenticação:
from django.contrib import auth

# Importa biblioteca de Alertas e mensagens do django:
from django.contrib import messages

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)
        # Verifica se o formulário é valido:
        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()
        # Usar o metodo de verificação do Django para realizar a validação:
        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha,
        )
        # Caso tudo esteja ok, redireciona para o index de galeria:
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} logado com sucesso!")
            return redirect('index')
        # Se não, redireciona para o login novamente.
        else:
            messages.error(request, "Erro ao efetuar login")
            return redirect('login')
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        # Verifica se o formulário é valido:
        if form.is_valid():
            # Verifica se as senhas são iguais:
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, "Senhas não são iguais")
                return redirect('cadastro')
            # Pega os dados de cada campo do form:
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_1"].value()
            # Verifica se ja existe o usuario cadastrado pelo login:
            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existente")
                return redirect('cadastro')
            # Criar o usuario no banco:
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect('login')
    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')
