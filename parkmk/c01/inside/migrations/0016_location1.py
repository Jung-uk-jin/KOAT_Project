# Generated by Django 5.1.4 on 2024-12-11 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inside', '0015_location_inform_l_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location1',
            fields=[
                ('lo_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]