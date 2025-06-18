from django.contrib import admin
from .models import Enquete, Opcao

class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 4

class EnqueteAdmin(admin.ModelAdmin):
    list_display = ('pergunta', 'data_criacao', 'data_encerramento', 'encerrada')
    inlines = [OpcaoInline]

admin.site.register(Enquete, EnqueteAdmin)

