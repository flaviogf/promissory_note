# Generated by Django 2.1.7 on 2019-03-18 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conta',
            options={'ordering': ('data_recebimento',)},
        ),
    ]
