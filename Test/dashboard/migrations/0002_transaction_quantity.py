# Generated by Django 5.2 on 2025-04-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
