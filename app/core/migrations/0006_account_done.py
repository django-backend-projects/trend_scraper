# Generated by Django 4.1.5 on 2023-02-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_account_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Bağlamalar bitib'),
        ),
    ]
