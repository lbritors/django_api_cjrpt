from django.contrib import admin
from .models import  Usuario, Professor, Disciplina, Avaliacao,Comentario
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Avaliacao)
admin.site.register(Comentario)
