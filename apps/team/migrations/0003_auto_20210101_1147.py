# Generated by Django 3.1.4 on 2021-01-01 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_invite'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Invite',
            new_name='Invitation',
        ),
    ]
