# Generated by Django 3.1.4 on 2020-12-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='id_tabela',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='RG',
            field=models.IntegerField(),
        ),
    ]
