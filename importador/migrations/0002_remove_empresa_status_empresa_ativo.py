# Generated by Django 4.0.1 on 2023-01-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importador', '0001_initial_manual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='status',
        ),
        migrations.AddField(
            model_name='empresa',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]