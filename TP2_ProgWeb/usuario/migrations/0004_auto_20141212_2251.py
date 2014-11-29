# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_aluno_aluno_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='professor_endereco',
            field=models.TextField(null=True, verbose_name=b'Endereco', blank=True),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
    ]
