# Generated by Django 3.1.5 on 2023-12-01 21:54

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('berweuli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='menu_images')),
                ('order', models.IntegerField(default=0, help_text='Menülerin sıralanması için buradan sıra numarası verilmesi gerekiyor.')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, max_length=500)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('cookingTime', models.IntegerField(default=0, help_text='Menünün Hazırlanma süresini giriniz.')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='berweuli.categorymodel')),
            ],
            options={
                'verbose_name': 'Menü',
                'verbose_name_plural': 'Menüler',
                'db_table': 'Menü',
                'ordering': ('order',),
            },
        ),
    ]
