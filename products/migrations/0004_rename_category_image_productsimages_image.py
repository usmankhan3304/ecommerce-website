# Generated by Django 4.2.2 on 2023-07-30 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_category_alter_productsimages_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsimages',
            old_name='category_image',
            new_name='image',
        ),
    ]
