# Generated by Django 5.0.6 on 2024-08-10 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0046_alter_price_chart_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_chart',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.productcategory'),
        ),
    ]