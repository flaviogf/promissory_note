# Generated by Django 2.1.7 on 2019-03-20 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190320_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='promisoria',
            name='baixada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='promisoria',
            name='data_baixa',
            field=models.DateField(blank=True, null=True),
        ),
    ]
