# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-12-24 11:15
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bilgi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120, verbose_name='Adi')),
                ('Surname', models.CharField(max_length=120, verbose_name='Soyadi')),
                ('content', models.TextField(verbose_name='Egitim_Bilgileri')),
                ('experience', models.TextField(verbose_name='Tecrube')),
                ('hobi', ckeditor.fields.RichTextField(verbose_name='Hobi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('job', models.CharField(max_length=120, verbose_name='Meslek')),
                ('language', models.TextField(verbose_name='Dil')),
                ('adress', models.TextField(verbose_name='Adres')),
                ('phone', models.CharField(max_length=11, verbose_name='Telefon')),
                ('email', models.EmailField(max_length=254, verbose_name='Mail')),
                ('date', models.DateField(verbose_name='Dogum_Tarihi')),
                ('dogumyeri', models.CharField(max_length=120, verbose_name='Dogum_Yeri')),
                ('medeni_hali', models.CharField(choices=[('evli', 'EVLİ'), ('bekar', 'BEKAR')], default='bekar', max_length=6)),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
