from django.db import models
from django.conf import settings



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Artigo(models.Model):
    """
    Modelo unificado para todos os tipos de artigos.
    """
    TIPO_CHOICES = [
        ('principal', 'Principal'),
        ('secundario', 'Secundário'),
        ('terciario', 'Terciário'),
        ('generico', 'Genérico'),
        ('recomendado', 'Recomendado'),
    ]

    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.titulo
