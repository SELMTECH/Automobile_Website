# Generated by Django 5.1.3 on 2024-12-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price_per_day',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
