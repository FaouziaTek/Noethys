# Generated by Django 3.2.25 on 2024-12-05 16:55

import core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0180_auto_20241129_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur_Individu',
            fields=[
            ],
            options={
                'verbose_name': 'Individu',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.utilisateur',),
            managers=[
                ('objects', core.models.CustomUserManager()),
            ],
        ),
    ]
