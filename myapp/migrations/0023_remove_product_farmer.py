# Generated by Django 5.0.6 on 2024-08-02 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_product_farmer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='farmer',
        ),
    ]
