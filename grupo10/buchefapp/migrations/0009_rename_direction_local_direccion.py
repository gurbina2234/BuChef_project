# Generated by Django 3.2.25 on 2024-07-15 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buchefapp', '0008_local_category_category_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='local',
            old_name='direction',
            new_name='direccion',
        ),
    ]
