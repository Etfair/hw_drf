# Generated by Django 4.2.4 on 2023-09-17 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='owner',
            new_name='user',
        ),
    ]