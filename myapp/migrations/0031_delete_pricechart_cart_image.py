# Generated by Django 5.0.6 on 2024-08-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_price_chart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PriceChart',
        ),
        migrations.AddField(
            model_name='cart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cart/'),
        ),
    ]