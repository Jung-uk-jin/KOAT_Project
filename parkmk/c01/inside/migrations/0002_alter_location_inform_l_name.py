# Generated by Django 5.1.4 on 2024-12-09 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inside', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location_inform',
            name='l_name',
            field=models.CharField(max_length=30),
        ),
    ]
