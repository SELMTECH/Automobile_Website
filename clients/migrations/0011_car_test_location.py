# Generated by Django 5.0.6 on 2024-06-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_car_price_car_test_drive_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='test_location',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]