from django import forms
from django.core.mail.message import EmailMessage

from .models import Produto

class ContatoForm(forms.Form):

  nome = forms.CharField(label='Nome', max_length=100)
  email = forms.CharField(label='E-mail', max_length=100)
  assunto = forms.CharField(label='Assunto', max_length=120)
  menssagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

  def send_email(self):
    nome = self.cleaned_data['nome']
    email = self.cleaned_data['email']
    assunto = self.cleaned_data['assunto']
    menssagem = self.cleaned_data['menssagem']

    conteudo = f'Nome: {nome} \n Email: {email} \n Assunto: {assunto} \n Menssagem: {menssagem} \n'

    mail = EmailMessage(
      subject='E-mail enviado pelo sistema django2',
      body=conteudo,
      from_email='contato@seudominio.com.br',
      to=['contato@seudominio.com.br', email],
      headers={'Reply-to': email}
    )
    mail.send()
  
class ProdutoModelForm(forms.ModelForm):
    class Meta:
      model = Produto
      fields = ['nome', 'preco', 'estoque', 'image']

