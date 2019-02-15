# Generated by Django 2.1.7 on 2019-02-15 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contatos', '0003_auto_20190214_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
