# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20141203_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='aluno_matricula',
            field=models.CharField(default=0, max_length=15, verbose_name=b'Matricula', blank=True),
            preserve_default=False,
        ),
    ]
