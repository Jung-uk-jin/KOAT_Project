# Generated by Django 5.1.3 on 2024-12-03 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_remove_board_bfile_board_b_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='b_file',
        ),
        migrations.AddField(
            model_name='board',
            name='bfile',
            field=models.ImageField(blank=True, null=True, upload_to='board'),
        ),
    ]
