# Generated by Django 4.0.1 on 2022-06-23 13:01

from django.db import migrations, models
import xmltoexcel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasta', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to=xmltoexcel.models.localsalvar)),
            ],
        ),
    ]