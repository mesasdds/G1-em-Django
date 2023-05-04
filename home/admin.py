from django.contrib import admin
# Register your models here.
from .models import ArtigoPrincipal, ArtigoSecundario, ArtigoTerceiro, ArtigosGenericos

admin.site.register(ArtigoPrincipal)
admin.site.register(ArtigoSecundario)
admin.site.register(ArtigoTerceiro)
admin.site.register(ArtigosGenericos)