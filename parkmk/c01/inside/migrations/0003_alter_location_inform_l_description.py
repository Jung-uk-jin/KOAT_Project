# Generated by Django 5.1.4 on 2024-12-09 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inside', '0002_alter_location_inform_l_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location_inform',
            name='l_description',
            field=models.CharField(max_length=1000),
        ),
    ]
