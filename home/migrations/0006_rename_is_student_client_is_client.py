# Generated by Django 4.2.9 on 2024-04-05 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_client_is_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='is_student',
            new_name='is_client',
        ),
    ]