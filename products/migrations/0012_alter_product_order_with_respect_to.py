# Generated by Django 3.2 on 2022-02-08 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20220208_1613'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='product',
            order_with_respect_to='name',
        ),
    ]
