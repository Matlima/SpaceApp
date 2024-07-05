from django.contrib import admin

from galeria.models import Fotografia

# Personalizando admin:
class ListandoFotografias(admin.ModelAdmin):
    # Exibindo campos inves do nome do objeto
    list_display = ("id", "nome", "legenda")
    # Adicionando link ao clicar na lista da tabela
    list_display_links = ("id", "nome")
    # Adicionando campo de busca no admin:
    search_fields = ("nome",)

# Envio de dados para mostrar no admin:
admin.site.register(Fotografia, ListandoFotografias)


