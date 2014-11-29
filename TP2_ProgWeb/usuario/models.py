from django.db import models
from django.contrib.auth.models import User
from usuario.choices import STATE_CHOICES#, LOGRADOURO_CHOICES

# Create your models here.

# class Endereco(models.Model):
#     endereco_id = models.AutoField(primary_key=True)
#     endereco_tipo_logradouro = models.CharField(max_length=10, choices=LOGRADOURO_CHOICES, verbose_name='Tipo Logradouro')
#     endereco_logradouro = models.CharField(max_length=80, verbose_name='Logradouro')
#     endereco_numero = models.IntegerField(verbose_name='Numero')
#     endereco_complemento = models.CharField(max_length=45, blank=True, verbose_name='Complemento')
#     endereco_bairro = models.CharField(max_length=80, verbose_name='Bairro')
#     endereco_cidade = models.CharField(max_length=80, verbose_name='Cidade')
#     endereco_estado = models.CharField(max_length=2, choices=STATE_CHOICES, verbose_name='Estado')
#     endereco_cep = models.CharField(max_length=9, blank=True, verbose_name='CEP')
#     def __unicode__(self):
#         return '%s %s, %s, %s, %s - %s' % (self.endereco_tipo_logradouro, self.endereco_logradouro, self.endereco_numero, self.endereco_bairro, self.endereco_cidade, self.endereco_estado)
#     class Meta:
#         db_table = 'Endereco'
#         verbose_name = 'Endereco'
#         verbose_name_plural = 'Enderecos'
#         ordering = ['endereco_tipo_logradouro']

class Professor(User):
    user = models.OneToOneField(User, parent_link = True)
    professor_telefone = models.CharField(max_length = 15, verbose_name = 'Telefone', blank = True, null = True)
    professor_numero_da_sala = models.IntegerField(blank = True, verbose_name = 'Numero da Sala', null = True)
#     professor_endereco = models.ForeignKey(Endereco, blank = True, null = True)
#     professor_endereco = models.TextField(verbose_name = 'Endereco', blank = True, null = True)
#     endereco_numero = models.IntegerField(verbose_name='Numero')
#     endereco_complemento = models.CharField(max_length=45, blank=True, verbose_name='Complemento')
    professor_endereco_logradouro = models.TextField(verbose_name='Logradouro', blank = True, null = True)
    professor_endereco_bairro = models.CharField(max_length=80, verbose_name='Bairro', blank = True, null = True)
    professor_endereco_cidade = models.CharField(max_length=80, verbose_name='Cidade', blank = True, null = True)
    professor_endereco_estado = models.CharField(max_length=2, choices=STATE_CHOICES, verbose_name='Estado', blank = True, null = True)
    professor_endereco_cep = models.CharField(max_length=9, verbose_name='CEP', blank = True, null = True)
    
    def __unicode__(self):
        return self.user.name
    
    class Meta:
        db_table = 'Professor'
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

class Aluno(User):
    user = models.OneToOneField(User, parent_link = True)
    aluno_matricula = models.CharField(max_length = 15, verbose_name = 'Matricula', blank = True)
    
    def __unicode__(self):
        return self.user.name
    
    class Meta:
        db_table = 'Aluno'
