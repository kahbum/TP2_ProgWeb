# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20141212_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='professor_endereco',
        ),
        migrations.AddField(
            model_name='professor',
            name='professor_endereco_bairro',
            field=models.CharField(max_length=80, null=True, verbose_name=b'Bairro', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professor',
            name='professor_endereco_cep',
            field=models.CharField(max_length=9, null=True, verbose_name=b'CEP', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professor',
            name='professor_endereco_cidade',
            field=models.CharField(max_length=80, null=True, verbose_name=b'Cidade', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professor',
            name='professor_endereco_estado',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name=b'Estado', choices=[(b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AP', b'Amapa'), (b'AM', b'Amazonas'), (b'BA', b'Bahia'), (b'CE', b'Ceara'), (b'DF', b'Distrito Federal'), (b'ES', b'Espirito Santo'), (b'GO', b'Goias'), (b'MA', b'Maranhao'), (b'MT', b'Mato Grosso'), (b'MS', b'Mato Grosso do Sul'), (b'MG', b'Minas Gerais'), (b'PA', b'Para'), (b'PB', b'Paraiba'), (b'PR', b'Parana'), (b'PE', b'Pernambuco'), (b'PI', b'Piaui'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RS', b'Rio Grande do Sul'), (b'RO', b'Rondonia'), (b'RR', b'Roraima'), (b'SC', b'Santa Catarina'), (b'SP', b'Sao Paulo'), (b'SE', b'Sergipe'), (b'TO', b'Tocantins')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professor',
            name='professor_endereco_logradouro',
            field=models.TextField(null=True, verbose_name=b'Logradouro', blank=True),
            preserve_default=True,
        ),
    ]
