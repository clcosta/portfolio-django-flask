from django.contrib import admin
from portfolio.models import Projeto

# Register your models here.

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    fields = ('titulo','link_codigo','iframe_video',('capa'))
    list_display = [('titulo'),('id')]
    search_fields = ('titulo', 'id')
    list_filter = ('id', 'titulo')
