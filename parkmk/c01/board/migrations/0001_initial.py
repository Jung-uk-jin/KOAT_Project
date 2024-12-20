# Generated by Django 5.1.3 on 2024-12-03 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0002_alter_member_m_auth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_no', models.IntegerField(max_length=10)),
                ('b_title', models.CharField(max_length=30)),
                ('b_content', models.CharField(max_length=1000)),
                ('b_hit', models.IntegerField(default=0)),
                ('b_header', models.CharField(max_length=10)),
                ('b_date', models.DateField(auto_now=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
    ]
