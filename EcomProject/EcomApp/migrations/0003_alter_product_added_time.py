# Generated by Django 5.1.4 on 2024-12-23 15:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomApp', '0002_product_img_alter_product_added_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
