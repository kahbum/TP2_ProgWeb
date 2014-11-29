# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='professor_endereco',
            field=models.ForeignKey(blank=True, to='usuario.Endereco', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='professor_numero_da_sala',
            field=models.IntegerField(null=True, verbose_name=b'Numero da Sala', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='professor_telefone',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Telefone', blank=True),
            preserve_default=True,
        ),
    ]
