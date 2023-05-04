from django.db import models
from django.utils import timezone

class ArtigoPrincipal(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='templates/home/media', blank=True, null=True)
    def __str__(self):
        return self.titulo

    
    #imagem = models.ImageField(upload_to='imagens/artigoprincipal/', blank=True)

class ArtigoSecundario(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='templates/home/media', blank=True, null=True)
    def __str__(self):
        return self.titulo
    #imagem = models.ImageField(upload_to='imagens/artigosecundario/', blank=True)

class ArtigoTerceiro(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='templates/home/media', blank=True, null=True)
    def __str__(self):
        return self.titulo


class ArtigosGenericos(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)
    def __str__(self):
        return self.titulo


