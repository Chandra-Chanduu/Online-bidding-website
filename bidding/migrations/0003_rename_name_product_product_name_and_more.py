# Generated by Django 5.0.2 on 2024-03-04 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]