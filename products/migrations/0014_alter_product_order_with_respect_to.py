# Generated by Django 3.2 on 2022-02-08 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_product_order_with_respect_to'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='product',
            order_with_respect_to='name',
        ),
    ]
