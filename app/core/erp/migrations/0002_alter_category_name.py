# Generated by Django 3.2.6 on 2021-08-11 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]
