# Generated by Django 5.1.4 on 2024-12-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inside', '0004_location_inform_l_description2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location_inform',
            name='l_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='location_inform',
            name='l_description2',
            field=models.CharField(max_length=1000),
        ),
    ]
