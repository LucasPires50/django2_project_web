from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        print(f'Post: {request.POST}')

        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            menssagem = form.cleaned_data['menssagem']

            print('Menssagem enviada')
            print(f'{nome} \n {email} \n {assunto} \n {menssagem}')

            messages.success(request, "E-mail enviado com sucesso!")
            form = ContatoForm()
        else:
            messages.error(request, "Error ao enviar o e-mail.")

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')
