# Generated by Django 5.0.2 on 2024-02-19 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0004_remove_practice_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parnter',
            name='full_name',
        ),
    ]