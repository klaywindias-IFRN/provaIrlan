from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Atleta,Equipe,Modalidade,Tecnico

# Register your models here.
admin.site.register(Atleta)
admin.site.register(Equipe)
admin.site.register(Modalidade)
admin.site.register(Tecnico)

 
@admin.register(Atleta)
class Atleta(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'equipe']
    list_filter = ['equipe', 'modalidade']
    search_fields =[ 'nome']
    
    
@admin.register(Equipe)
class Equipe(admin):
    list_display = ['nome', 'curso', 'quantidade_atletas']
    list_filter = ['equipe', 'modalidade']
    search_fields =[ 'nome']
    
    