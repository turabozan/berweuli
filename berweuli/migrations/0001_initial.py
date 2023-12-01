# Generated by Django 3.1.5 on 2023-12-01 21:29

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='Kategorilerin sıralanması için buradan sıra numarası verilmesi gerekiyor.')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('categoryData', models.CharField(max_length=100)),
                ('menuData', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
                'db_table': 'Kategori',
                'ordering': ('order',),
            },
        ),
    ]