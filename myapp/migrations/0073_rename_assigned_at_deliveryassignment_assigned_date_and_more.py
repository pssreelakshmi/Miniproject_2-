# Generated by Django 5.0.6 on 2024-08-28 13:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0072_remove_payment_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveryassignment',
            old_name='assigned_at',
            new_name='assigned_date',
        ),
        migrations.AddField(
            model_name='deliveryassignment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliveryassignment',
            name='delivery_boy',
            field=models.ForeignKey(limit_choices_to={'role': 'deliveryboy'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]