# Generated by Django 4.2.17 on 2025-01-02 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_usuario_senha'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]