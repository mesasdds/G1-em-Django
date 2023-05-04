from django.contrib import admin
# Register your models here.
from .models import ArtigoPrincipal, ArtigoSecundario, ArtigoTerceiro, ArtigosGenericos, ArtigosRecommends

admin.site.register(ArtigoPrincipal)
admin.site.register(ArtigoSecundario)
admin.site.register(ArtigoTerceiro)
admin.site.register(ArtigosGenericos)
admin.site.register(ArtigosRecommends)