# Generated by Django 5.1.3 on 2024-12-12 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_comment_c_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='c_comment',
            new_name='parent_comment',
        ),
    ]
