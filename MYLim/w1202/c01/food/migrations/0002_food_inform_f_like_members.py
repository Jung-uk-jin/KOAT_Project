# Generated by Django 5.1.3 on 2024-12-16 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_inform',
            name='f_like_members',
            field=models.ManyToManyField(default='', related_name='food_like_member', to='member.member'),
        ),
    ]
