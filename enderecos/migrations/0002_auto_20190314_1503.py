# Generated by Django 2.1.7 on 2019-03-14 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='endereco',
            options={'ordering': ('cep',)},
        ),
    ]
