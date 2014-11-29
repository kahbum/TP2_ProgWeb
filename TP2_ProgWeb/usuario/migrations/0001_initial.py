# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('user', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Aluno',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('endereco_id', models.AutoField(serialize=False, primary_key=True)),
                ('endereco_tipo_logradouro', models.CharField(max_length=10, verbose_name=b'Tipo Logradouro', choices=[('rua', 'Rua'), ('avenida', 'Avenida'), ('travessa', 'Travessa')])),
                ('endereco_logradouro', models.CharField(max_length=80, verbose_name=b'Logradouro')),
                ('endereco_numero', models.IntegerField(verbose_name=b'Numero')),
                ('endereco_complemento', models.CharField(max_length=45, verbose_name=b'Complemento', blank=True)),
                ('endereco_bairro', models.CharField(max_length=80, verbose_name=b'Bairro')),
                ('endereco_cidade', models.CharField(max_length=80, verbose_name=b'Cidade')),
                ('endereco_estado', models.CharField(max_length=2, verbose_name=b'Estado', choices=[(b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AP', b'Amapa'), (b'AM', b'Amazonas'), (b'BA', b'Bahia'), (b'CE', b'Ceara'), (b'DF', b'Distrito Federal'), (b'ES', b'Espirito Santo'), (b'GO', b'Goias'), (b'MA', b'Maranhao'), (b'MT', b'Mato Grosso'), (b'MS', b'Mato Grosso do Sul'), (b'MG', b'Minas Gerais'), (b'PA', b'Para'), (b'PB', b'Paraiba'), (b'PR', b'Parana'), (b'PE', b'Pernambuco'), (b'PI', b'Piaui'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RS', b'Rio Grande do Sul'), (b'RO', b'Rondonia'), (b'RR', b'Roraima'), (b'SC', b'Santa Catarina'), (b'SP', b'Sao Paulo'), (b'SE', b'Sergipe'), (b'TO', b'Tocantins')])),
                ('endereco_cep', models.CharField(max_length=9, verbose_name=b'CEP', blank=True)),
            ],
            options={
                'ordering': ['endereco_tipo_logradouro'],
                'db_table': 'Endereco',
                'verbose_name': 'Endereco',
                'verbose_name_plural': 'Enderecos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('professor_telefone', models.CharField(max_length=15, verbose_name=b'Telefone', blank=True)),
                ('professor_numero_da_sala', models.IntegerField(verbose_name=b'Numero da Sala', blank=True)),
                ('professor_endereco', models.ForeignKey(to='usuario.Endereco', blank=True)),
            ],
            options={
                'db_table': 'Professor',
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
            },
            bases=('auth.user',),
        ),
    ]
