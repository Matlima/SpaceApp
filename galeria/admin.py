from django.contrib import admin

# Importando Model de galeria:
from galeria.models import Fotografia

# Personalizando admin:
class ListandoFotografias(admin.ModelAdmin):
    # Exibindo campos inves do nome do objeto
    list_display = ("id", "nome", "legenda", "publicada")
    # Adicionando link ao clicar na lista da tabela
    list_display_links = ("id", "nome")
    # Adicionando campo de busca no admin:
    search_fields = ("nome",)
    # Adicionando filtro por categoria e usuário:
    list_filter = ("categoria","usuario",)
    # Adicionando para editar o publicado diretamente:
    list_editable = ("publicada",)
    # Adicionando paginação no admin:
    list_per_page = 10
    

# Envio de dados para mostrar no admin:
admin.site.register(Fotografia, ListandoFotografias)


