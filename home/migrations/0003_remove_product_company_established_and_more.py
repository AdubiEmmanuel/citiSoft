# Generated by Django 4.2.9 on 2024-03-28 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_name_product_location_cities_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='company_established',
        ),
        migrations.RemoveField(
            model_name='product',
            name='contact_telephone_no',
        ),
        migrations.RemoveField(
            model_name='product',
            name='internal_professional_services',
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_demo_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_reviewed_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='location_cities',
        ),
        migrations.RemoveField(
            model_name='product',
            name='no_of_employees',
        ),
    ]