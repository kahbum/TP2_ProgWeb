from django.contrib import admin
from usuario.models import Professor, Aluno#, Endereco
from disciplina.models import Disciplina, Tarefa

# Register your models here.

admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Tarefa)
# admin.site.register(Endereco)