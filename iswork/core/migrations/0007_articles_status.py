# Generated by Django 2.2 on 2020-06-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200607_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус заявки'),
        ),
    ]
