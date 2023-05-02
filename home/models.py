from django.db import models

class ArtigoPrincipal(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    #imagem = models.ImageField(upload_to='imagens/artigoprincipal/', blank=True)

class ArtigoSecundario(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    #imagem = models.ImageField(upload_to='imagens/artigosecundario/', blank=True)

class ArtigoTerceiro(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()