# Generated by Django 5.0.4 on 2025-01-15 03:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0018_alter_categoria_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 15, 0, 4, 7, 272658)),
        ),
        migrations.AlterField(
            model_name='livros',
            name='co_autor',
            field=models.CharField(blank=True, max_length=30, verbose_name='Coautor'),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(default=datetime.date.today, verbose_name='Data do Cadastro'),
        ),
        migrations.AlterField(
            model_name='livros',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='capa_livro', verbose_name='Capa do Livro'),
        ),
    ]
