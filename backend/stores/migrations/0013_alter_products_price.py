# Generated by Django 3.2.9 on 2022-10-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0012_alter_products_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]
