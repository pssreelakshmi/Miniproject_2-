# Generated by Django 5.0.6 on 2024-08-23 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0059_order_order_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]