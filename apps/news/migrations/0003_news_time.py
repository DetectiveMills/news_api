# Generated by Django 5.1.1 on 2024-10-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='time',
            field=models.CharField(default=1, max_length=155, verbose_name='Дата'),
            preserve_default=False,
        ),
    ]
