# Generated by Django 3.2.8 on 2021-10-21 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desxription',
            new_name='description',
        ),
    ]
