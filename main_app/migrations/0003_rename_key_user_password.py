# Generated by Django 3.2.7 on 2021-10-14 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='key',
            new_name='password',
        ),
    ]
