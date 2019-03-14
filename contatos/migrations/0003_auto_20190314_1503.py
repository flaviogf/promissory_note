# Generated by Django 2.1.7 on 2019-03-14 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_auto_20190313_1831'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ('nome',)},
        ),
        migrations.AddField(
            model_name='contato',
            name='atualizado_em',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 15, 3, 50, 884808)),
        ),
        migrations.AddField(
            model_name='contato',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 15, 3, 50, 884786)),
        ),
    ]
