# Generated by Django 2.2.7 on 2020-05-07 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20200506_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('status', models.BooleanField(default=False, verbose_name='Видимость статьи')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_articles', to='core.Articles', verbose_name='Статья')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
            ],
        ),
    ]
