# Generated by Django 4.0.1 on 2022-01-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='title',
            field=models.CharField(default='Foo', max_length=100),
            preserve_default=False,
        ),
    ]
