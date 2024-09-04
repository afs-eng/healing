from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse
def login(request):
    if request.method == 'GET':
        return render(request, 'usuario/login.html')



def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuario/cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return render(request, 'usuario/cadastro.html')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe')
            return render(request, 'usuario/cadastro.html')

        user = User.objects.filter(email=email)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'E-mail já existe')
            return render(request, 'usuario/cadastro.html')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
        return render(request, 'usuario/login.html')





def logout(request):
    pass
