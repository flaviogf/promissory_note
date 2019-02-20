# Generated by Django 2.1.7 on 2019-02-20 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0007_historicoendereco'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ['-criado_em'], 'verbose_name': 'Contato', 'verbose_name_plural': 'Contatos'},
        ),
        migrations.AlterModelOptions(
            name='endereco',
            options={'ordering': ['-criado_em'], 'verbose_name': 'Endereço', 'verbose_name_plural': 'Endereços'},
        ),
        migrations.AlterModelOptions(
            name='historicocontato',
            options={'ordering': ['-atualizado_em'], 'verbose_name': 'Histórico Contato', 'verbose_name_plural': 'Históricos Contatos'},
        ),
        migrations.AlterModelOptions(
            name='historicoendereco',
            options={'ordering': ['-atualizado_em'], 'verbose_name': 'Histórico Endereço', 'verbose_name_plural': 'Históricos Endereços'},
        ),
    ]
