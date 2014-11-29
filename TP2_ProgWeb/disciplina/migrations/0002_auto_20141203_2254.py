# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa_aluno',
            name='aluno',
            field=models.ForeignKey(to='usuario.Aluno'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tarefa_aluno',
            name='tarefa',
            field=models.ForeignKey(to='disciplina.Tarefa'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='tarefa_aluno',
            unique_together=set([('tarefa', 'aluno')]),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='tarefa_disciplina',
            field=models.ForeignKey(to='disciplina.Disciplina'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplina_aluno',
            name='aluno',
            field=models.ForeignKey(to='usuario.Aluno'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplina_aluno',
            name='disciplina',
            field=models.ForeignKey(to='disciplina.Disciplina'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='disciplina_aluno',
            unique_together=set([('disciplina', 'aluno')]),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='disciplina_professor',
            field=models.ForeignKey(to='usuario.Professor'),
            preserve_default=True,
        ),
    ]
