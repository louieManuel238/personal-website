# Generated by Django 2.0.6 on 2018-06-26 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20180625_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='humbnail_url',
            new_name='thumbnail_url',
        ),
    ]
