# admin.py
from django.contrib import admin
from .models import ArtigoPrincipal, ArtigoSecundario, ArtigoTerceiro, ArtigosGenericos, ArtigosRecommends, Category, Tag

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'create_at', 'update_at')
    search_fields = ('titulo', 'texto')
    list_filter = ('categories', 'tags')

admin.site.register(ArtigoPrincipal, ArtigoAdmin)
admin.site.register(ArtigoSecundario, ArtigoAdmin)
admin.site.register(ArtigoTerceiro, ArtigoAdmin)
admin.site.register(ArtigosGenericos, ArtigoAdmin)
admin.site.register(ArtigosRecommends, ArtigoAdmin)
admin.site.register(Category)
admin.site.register(Tag)
