from django.db import models

# signals
from django.db.models import signals
from django.template.defaultfilters import slugify

from stdimage.models import StdImageField

"""
Uma classe abstrada não é criada no banco de dados, 
ela sever apenas de racunho para outras classes.
"""
class Base(models.Model):
  criado = models.DateField("Data de Criação", auto_now=False, auto_now_add=True)
  modificado = models.DateField("Data de Atualização", auto_now=True, auto_now_add=False)
  ativo = models.BooleanField("Ativo", default=True)

  class Meta:
    abstract =  True

"""
Esta extendendo a classe "Base"

No campo "IMAGE", tem o atributo "VARIATIONS", 
e que após ser salvo a imagem original, é salvo uma variação da imagem, 
aplicando as configurações definidas no "VARIANTIONS".

"""
class Produto(Base):
  nome = models.CharField("Nome", max_length=100)
  preco = models.DecimalField("Preço", max_digits=8, decimal_places=2)
  estoque = models.IntegerField("Estoque")
  image = StdImageField('Image', upload_to='produtos', variations={'thumb':(124, 124)})
  slug = models.SlugField("Slug", max_length=100, blank=True, editable=False)

  def __str__(self) -> str:
    return self.nome

"""
Vai adicionar o nome a campo "SLUG",
após ser feito o "SLUGIFY" no nome.
EX:
  Correia Dentada -> correia-dentada
"""
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

"""
Antes de salvar, execute a função "PRODUTO_PRE_SAVE", 
quando a variaves que está atribuida no "SENDER", submeter um sinal.

Nesse caso o sinal é quando o "PRODUTO", for salvo.
"""
signals.pre_save.connect(produto_pre_save, sender=Produto)