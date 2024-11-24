# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ArtigoBase(models.Model):
    """
    Classe base abstrata para os modelos de artigos.
    """
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.titulo


class ArtigoPrincipal(ArtigoBase):
    """
    Modelo para artigos principais.
    """
    pass


class ArtigoSecundario(ArtigoBase):
    """
    Modelo para artigos secundários.
    """
    pass


class ArtigoTerceiro(ArtigoBase):
    """
    Modelo para artigos terciários.
    """
    pass


class ArtigosGenericos(ArtigoBase):
    """
    Modelo para artigos genéricos.
    """
    pass


class ArtigosRecommends(ArtigoBase):
    """
    Modelo para artigos recomendados.
    """
    pass
