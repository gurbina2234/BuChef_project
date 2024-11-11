# Generated by Django 3.2.25 on 2024-07-14 21:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buchefapp', '0007_auto_20240714_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='local_category',
            name='category_count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
