# Generated by Django 5.0.2 on 2024-03-19 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='approved',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
