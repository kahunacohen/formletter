# Generated by Django 4.0.1 on 2022-01-09 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formletter', '0004_alter_letter_letter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='letter',
            new_name='template',
        ),
    ]
