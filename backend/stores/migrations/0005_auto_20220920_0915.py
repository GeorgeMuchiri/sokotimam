# Generated by Django 3.2.9 on 2022-09-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_alter_images_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
