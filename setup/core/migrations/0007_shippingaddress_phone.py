# Generated by Django 4.2.3 on 2023-07-19 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_oreder_customer_alter_shippingaddress_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(default=datetime.datetime(2023, 7, 19, 11, 2, 58, 615866, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
    ]