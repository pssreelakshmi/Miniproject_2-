# Generated by Django 5.0.6 on 2024-08-28 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0070_deliveryassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cart',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myapp.cart'),
            preserve_default=False,
        ),
    ]