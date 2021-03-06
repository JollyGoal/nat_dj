# Generated by Django 3.1.7 on 2021-02-24 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nat', '0003_auto_20210224_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ImageField(blank=True, help_text='Для новостей Главная картинка объязательна!', null=True, upload_to='images/', verbose_name='Главная Картинка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
    ]
