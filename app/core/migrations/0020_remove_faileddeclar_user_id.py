# Generated by Django 4.1.5 on 2023-09-09 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_declaration_is_declared'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faileddeclar',
            name='user_id',
        ),
    ]
