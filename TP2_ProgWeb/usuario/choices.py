# -*- coding: utf-8 -*-
"""
An alphabetical list of Brazilian states for use as `choices` in a formfield.
This exists in this standalone file so that it's only imported into memory
when explicitly needed.
"""

STATE_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapa'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceara'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espirito Santo'),
    ('GO', 'Goias'),
    ('MA', 'Maranhao'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Para'),
    ('PB', 'Paraiba'),
    ('PR', 'Parana'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piaui'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondonia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'Sao Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)

LOGRADOURO_CHOICES = (
    (u'rua', u'Rua'),
    (u'avenida', u'Avenida'),
    (u'travessa', u'Travessa')
)