# Generated by Django 4.2.9 on 2024-04-13 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_product_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='website',
            field=models.CharField(default=False, max_length=50),
        ),
    ]