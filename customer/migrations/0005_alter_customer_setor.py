# Generated by Django 4.0.1 on 2022-05-12 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customer_setor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='setor',
            field=models.PositiveSmallIntegerField(choices=[(1, 'FISCAL'), (2, 'CONTABILIDADE')], default=1),
        ),
    ]
