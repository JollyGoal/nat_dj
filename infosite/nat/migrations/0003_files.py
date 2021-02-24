# Generated by Django 3.1.7 on 2021-02-23 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nat', '0002_auto_20210223_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название Файла')),
                ('file', models.FileField(upload_to='files/', verbose_name='Документы (PDF, WORD...)')),
                ('documents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nat.post', verbose_name='Документы')),
            ],
        ),
    ]