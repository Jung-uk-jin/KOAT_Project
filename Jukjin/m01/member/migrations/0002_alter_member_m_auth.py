# Generated by Django 5.1.3 on 2024-12-03 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='m_auth',
            field=models.IntegerField(default=1),
        ),
    ]
