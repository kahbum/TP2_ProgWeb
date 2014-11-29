from django.db import models
from usuario.models import Aluno, Professor

# Create your models here.

class Disciplina(models.Model):
    disciplina_id = models.AutoField(primary_key = True)
    disciplina_professor = models.ForeignKey(Professor)
    disciplina_codigo = models.CharField(max_length = 10, unique = True, verbose_name = 'Codigo')
    disciplina_nome = models.CharField(max_length = 50, verbose_name = 'Nome')
    disciplina_ementa = models.TextField(blank = True, verbose_name = 'Ementa')
    disciplina_referencia_bibliografica = models.TextField(blank = True, verbose_name = 'Referencia Bibliografica')
    disciplina_numero_de_aulas = models.IntegerField(verbose_name = 'Numero de Aulas') 
    
    def __unicode__(self):
        return self.disciplina_nome
    
    class Meta:
        db_table = 'Disciplina'

class Disciplina_Aluno(models.Model):
    disciplina = models.ForeignKey(Disciplina)
    aluno = models.ForeignKey(Aluno)
    numero_de_presencas = models.IntegerField(verbose_name = 'Numero de Presencas')
    frequencia = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = 'Frequencia')
    nota = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = 'Nota')
    
    def __unicode__(self):
        return '%s - %s' %(self.disciplina, self.aluno)
    
    class Meta:
        db_table = 'Disciplina_Aluno'
        unique_together = ('disciplina', 'aluno')

class Tarefa(models.Model):
    tarefa_id = models.AutoField(primary_key = True)
    tarefa_disciplina = models.ForeignKey(Disciplina)
    tarefa_nome = models.CharField(max_length = 50, verbose_name = 'Nome')
    tarefa_descricao = models.TextField(blank = True, null = True, verbose_name = 'Descricao')
    tarefa_data_entrega = models.DateTimeField(blank = True, null = True, verbose_name = 'Data de Entrega')
    
    def __unicode__(self):
        return self.tarefa_nome
    
    class Meta:
        db_table = 'Tarefa'

class Tarefa_Aluno(models.Model):
    tarefa = models.ForeignKey(Tarefa)
    aluno = models.ForeignKey(Aluno)
    solucao = models.FileField(blank = True, null = True, verbose_name = 'Solucao')
    
    def __unicode__(self):
        return '%s - %s' % (self.tarefa_id, self.aluno_id)
    
    class Meta:
        db_table = 'Tarefa_Aluno'
        unique_together = ('tarefa', 'aluno')