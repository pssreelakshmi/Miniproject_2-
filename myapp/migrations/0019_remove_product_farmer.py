# Generated by Django 5.0.6 on 2024-07-30 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_remove_product_farmer_id_product_farmer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='farmer',
        ),
    ]