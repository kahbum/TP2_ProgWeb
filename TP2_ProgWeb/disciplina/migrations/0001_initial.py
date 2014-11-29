# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('disciplina_id', models.AutoField(serialize=False, primary_key=True)),
                ('disciplina_codigo', models.CharField(unique=True, max_length=10, verbose_name=b'Codigo')),
                ('disciplina_nome', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('disciplina_ementa', models.TextField(verbose_name=b'Ementa', blank=True)),
                ('disciplina_referencia_bibliografica', models.TextField(verbose_name=b'Referencia Bibliografica', blank=True)),
                ('disciplina_numero_de_aulas', models.IntegerField(verbose_name=b'Numero de Aulas')),
            ],
            options={
                'db_table': 'Disciplina',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disciplina_Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_de_presencas', models.IntegerField(verbose_name=b'Numero de Presencas')),
                ('frequencia', models.DecimalField(verbose_name=b'Frequencia', max_digits=5, decimal_places=2)),
                ('nota', models.DecimalField(verbose_name=b'Nota', max_digits=5, decimal_places=2)),
            ],
            options={
                'db_table': 'Disciplina_Aluno',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('tarefa_id', models.AutoField(serialize=False, primary_key=True)),
                ('tarefa_nome', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('tarefa_descricao', models.TextField(null=True, verbose_name=b'Descricao', blank=True)),
                ('tarefa_data_entrega', models.DateTimeField(null=True, verbose_name=b'Data de Entrega', blank=True)),
            ],
            options={
                'db_table': 'Tarefa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tarefa_Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('solucao', models.FileField(upload_to=b'', null=True, verbose_name=b'Solucao', blank=True)),
            ],
            options={
                'db_table': 'Tarefa_Aluno',
            },
            bases=(models.Model,),
        ),
    ]
