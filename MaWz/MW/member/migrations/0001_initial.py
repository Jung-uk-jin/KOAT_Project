# Generated by Django 5.1.3 on 2024-12-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('m_username', models.CharField(max_length=100)),
                ('m_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('m_password', models.CharField(max_length=100)),
                ('m_nickName', models.CharField(max_length=100)),
                ('m_email', models.CharField(max_length=100)),
                ('m_gender', models.CharField(default='남자', max_length=10)),
                ('m_date', models.DateTimeField(auto_now=True)),
                ('m_auth', models.IntegerField(default=1)),
            ],
        ),
    ]