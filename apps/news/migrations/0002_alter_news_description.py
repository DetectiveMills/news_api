# Generated by Django 5.1.1 on 2024-10-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(default='Описание новостей', verbose_name='Описание новостей'),
        ),
    ]
