# Generated by Django 4.1.2 on 2022-10-12 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='link',
            new_name='original_link',
        ),
        migrations.RenameField(
            model_name='url',
            old_name='uuid',
            new_name='short_link',
        ),
    ]
