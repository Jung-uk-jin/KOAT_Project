# Generated by Django 5.1.4 on 2024-12-10 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inside', '0013_location_inform_l_attraction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location_inform',
            name='l_attraction',
        ),
        migrations.AddField(
            model_name='attraction',
            name='a_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inside.location_inform'),
        ),
    ]
