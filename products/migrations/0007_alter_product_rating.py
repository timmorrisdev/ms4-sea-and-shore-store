# Generated by Django 3.2 on 2022-01-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]