# Generated by Django 3.0.2 on 2020-01-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0018_person_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='name_en',
            field=models.CharField(max_length=64, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_es',
            field=models.CharField(max_length=64, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_ru',
            field=models.CharField(max_length=64, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_uk',
            field=models.CharField(max_length=64, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_zh_hans',
            field=models.CharField(max_length=64, null=True, verbose_name='Name'),
        ),
    ]
