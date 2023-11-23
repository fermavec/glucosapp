# Generated by Django 2.2.3 on 2023-11-11 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('units', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading_value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readings.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
