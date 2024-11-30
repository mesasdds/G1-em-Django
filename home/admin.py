from django.contrib import admin
from .models import Artigo, Category, Tag

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'create_at', 'update_at')
    list_filter = ('tipo', 'categories', 'tags')
    search_fields = ('titulo', 'texto')

admin.site.register(Category)
admin.site.register(Tag)
