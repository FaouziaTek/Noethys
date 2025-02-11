# Generated by Django 3.2.21 on 2024-12-10 13:46

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0179_auto_20241205_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='comptaoperation',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=core.models.get_uuid_path, verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='activite',
            name='reattribution_adresse_exp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.adressemail', verbose_name="Adresse d'expédition"),
        ),
        migrations.AlterField(
            model_name='activite',
            name='reattribution_modele_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.modeleemail', verbose_name="Modèle d'Email"),
        ),
        migrations.AlterField(
            model_name='activite',
            name='validation_modele_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='validation_modele_email', to='core.modeleemail', verbose_name="Modèle d'Email"),
        ),
        migrations.AlterField(
            model_name='unite',
            name='heure_debut_fixe',
            field=models.BooleanField(default=False, help_text="Cochez cette case si vous souhaitez que l'utilisateur ne puisse pas modifier l'heure de début.", verbose_name='Heure de début fixe'),
        ),
        migrations.AlterField(
            model_name='unite',
            name='heure_fin_fixe',
            field=models.BooleanField(default=False, help_text="Cochez cette case si vous souhaitez que l'utilisateur ne puisse pas modifier l'heure de fin.", verbose_name='Heure de fin fixe'),
        ),
        migrations.AlterField(
            model_name='unite',
            name='imposer_saisie_valeur',
            field=models.BooleanField(default=False, verbose_name='Imposer la saisie de la valeur aux usagers sur le portail'),
        ),
    ]
