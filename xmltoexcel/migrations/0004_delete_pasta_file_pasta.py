# Generated by Django 4.0.1 on 2022-06-22 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xmltoexcel', '0003_pasta_remove_file_pasta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pasta',
        ),
        migrations.AddField(
            model_name='file',
            name='pasta',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]