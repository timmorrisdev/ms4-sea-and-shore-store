# Generated by Django 3.2 on 2022-01-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
