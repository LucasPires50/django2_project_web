from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':

        if form.is_valid():
            form.send_email()

            messages.success(request, "E-mail enviado com sucesso!")
            form = ContatoForm()
        else:
            messages.error(request, "Error ao enviar o e-mail.")

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == "POST":
        form = ProdutoModelForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            prod = form.save(commit=False)
            print(f"Nome: {prod.nome}, \n Preço: {prod.preco}, \n Estoque: {prod.estoque}, \n Imagem: {prod.image},")
            messages.success(request, "Produto salvo com sucesso.")
            form = ProdutoModelForm()
        else:
            messages.error(request, "Error ao salvar produto.")
    else:
        form = ProdutoModelForm()

    context = {
        'form': form
    }

    return render(request, 'produto.html', context)
