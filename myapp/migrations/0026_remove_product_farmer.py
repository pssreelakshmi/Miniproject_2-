# Generated by Django 5.0.6 on 2024-08-07 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_product_farmer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='farmer',
        ),
    ]