# Generated by Django 5.0.2 on 2024-02-19 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parnter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('full_name', models.TextField()),
                ('image', models.URLField(verbose_name=1000)),
                ('agreement', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.parnter')),
            ],
        ),
        migrations.CreateModel(
            name='DocLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
                ('url', models.URLField(max_length=1000)),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.practice')),
            ],
        ),
    ]
